from fastapi import FastAPI
from copy import deepcopy

from data.zones import zones
from services.graph_service import build_graph
from services.score_service import get_max_values, calculate_score
from services.optimizer_service import optimize_zones
from services.plant_service import plant_trees
from utils.validator import validate_zones
from services.species_service import get_species_mix

from schemas.api_models import (
    PlantRequest,
    PlantResponse,
    OptimizedZone,
    OptimizeResponse
)

app = FastAPI(title="GreenLedger API")

# -------------------------------
# INITIAL SETUP (runs once)
# -------------------------------

validate_zones(zones)
graph = build_graph()

from services.score_service import apply_scores

apply_scores(zones)


# -------------------------------
# API 1: Get all zones
# -------------------------------
@app.get("/zones")
def get_zones():
    return zones


# -------------------------------
# API 2: Optimize zones
# -------------------------------
@app.get("/optimize", response_model=OptimizeResponse)
def get_optimized_zones(k: int = 3):

    temp_zones = deepcopy(zones)

    result = optimize_zones(graph, temp_zones, k)

    selected = result["selected_zones"]
    allocation = result["allocation"]

    response = [
        OptimizedZone(
            id=z,
            name=temp_zones[z]["name"],
            score=round(temp_zones[z]["score"], 2),
            saplings=allocation.get(z, 0),
            species=get_species_mix(temp_zones[z],allocation.get(z, 0))
        )
        for z in selected
    ]

    return OptimizeResponse(
        zones=response,
        saplings_left=result["saplings_left"]
    )


# -------------------------------
# API 3: Plant trees (STATE CHANGE)
# -------------------------------
@app.post("/plant", response_model=PlantResponse)
def plant(request: PlantRequest):

    result = plant_trees(graph, zones, request.allocation)

    return PlantResponse(
        message="Planting applied successfully",
        before=result["before"],
        after=result["after"],
        impact=result["impact"]   
    )


# -------------------------------
# ROOT
# -------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to the GreenLedger API!"}