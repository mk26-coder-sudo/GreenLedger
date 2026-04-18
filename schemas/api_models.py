from pydantic import BaseModel
from typing import List

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

class OptimizeResponse(BaseModel):
    zones: List[OptimizedZone]