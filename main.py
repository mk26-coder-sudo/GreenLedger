from data.zones import zones
from services.graph_service import build_graph
from services.score_service import get_max_values, calculate_score
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
# STEP 3: Print Scores (debug)
# -------------------------------
print("\nZone Scores:")
for z in zones.values():
    print(z["name"], "->", z["score"])

# -------------------------------
# STEP 4: Build Max Heap
# -------------------------------
heap = []

for zone_id, zone in zones.items():
    heapq.heappush(heap, (-zone["score"], zone_id))

# -------------------------------
# STEP 5: Get Top Priority Zone
# -------------------------------
top = heapq.heappop(heap)

print("\nTop Priority Zone:")
print("Zone:", zones[top[1]]["name"])
print("Score:", -top[0])

# push it back (so heap remains intact)
heapq.heappush(heap, top)