from pydantic import BaseModel
from typing import Dict, List

class Zone(BaseModel):
    id: int
    name: str
    ndvi: float
    population: int
    heat: float
    flood_risk: float
    score: float

class OptimizedZone(BaseModel):
    id: int
    name: str
    score: float
    saplings: int

class OptimizeResponse(BaseModel):
    zones: List[OptimizedZone]
    saplings_left: int

class PlantRequest(BaseModel):
    allocation: Dict[int, int]


class PlantResponse(BaseModel):
    message: str
    before: dict
    after: dict
    impact: Dict[int, float]