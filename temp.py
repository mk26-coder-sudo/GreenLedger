from data.zones import zones
from services.graph_service import build_graph
from services.score_service import apply_scores

# graph = build_graph()

# for node, edges in graph.items():
#     print("\n", node, "->")
#     for e in edges:
#         print("   ", e)

apply_scores(zones)
for z in zones.values():
    print(z["name"], z["score"], z["mandatory"])