from data.zones import zones
from services.graph_service import build_graph
from services.score_service import get_max_values, calculate_score

# build graph
graph = build_graph()

# calculate scores
max_pop, max_heat = get_max_values()

for zone_id, zone in zones.items():
    zone["score"] = calculate_score(zone, max_pop, max_heat)

# print results
for z in zones.values():
    print(z["name"], "->", z["score"])