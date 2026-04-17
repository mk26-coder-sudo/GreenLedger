from data.zones import zones
from services.graph_service import build_graph
from services.score_service import get_max_values, calculate_score
from services.optimizer_service import optimize_zones
import heapq

# -------------------------------
# STEP 1: Build Graph
# -------------------------------
graph = build_graph()

# -------------------------------
# STEP 2: Calculate Scores
# -------------------------------
max_pop, max_heat = get_max_values()

for zone_id, zone in zones.items():
    zone["score"] = calculate_score(zone, max_pop, max_heat)

# -------------------------------
# STEP 3: Print Scores
# -------------------------------
print("\nZone Scores:")
for z in zones.values():
    print(z["name"], "->", z["score"])

# -------------------------------
# STEP 4: Heap (Top Zone)
# -------------------------------
heap = []

for zone_id, zone in zones.items():
    heapq.heappush(heap, (-zone["score"], zone_id))

top = heapq.heappop(heap)

print("\nTop Priority Zone:")
print("Zone:", zones[top[1]]["name"])
print("Score:", -top[0])

heapq.heappush(heap, top)

# -------------------------------
# STEP 5: OPTIMIZER ( MAIN)
# -------------------------------
selected = optimize_zones(graph, zones, k=3)

print("\nOptimized Zones for Planting:")
for i in range(2):
    selected = optimize_zones(graph, zones, k=3)
    print("Round", i+1, ":", [zones[z]["name"] for z in selected])