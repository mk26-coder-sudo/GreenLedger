from fastapi import FastAPI
from data.zones import zones
from services.graph_service import build_graph
from services.score_service import get_max_values, calculate_score
from services.optimizer_service import optimize_zones
from schemas.api_models import OptimizeResponse, OptimizedZone
from copy import deepcopy

app = FastAPI(title="GreenLedger API")

# -------------------------------
# INITIAL SETUP (runs once)
# -------------------------------
graph = build_graph()

max_pop, max_heat = get_max_values()

for zone_id, zone in zones.items():
    zone["score"] = calculate_score(zone, max_pop, max_heat)

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

    response = []

    for z in selected:
        response.append(
            OptimizedZone(
                id=z,
                name=temp_zones[z]["name"],
                score=round(temp_zones[z]["score"], 2),
                saplings=allocation.get(z, 0)   # IMPORTANT FIX
            )
        )

    return {
        "zones": response,
        "saplings_left": result["saplings_left"]
    }
@app.get("/")
def root():
    return {"message": "Welcome to the GreenLedger API!"}