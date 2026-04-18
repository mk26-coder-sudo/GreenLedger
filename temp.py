from services.graph_service import build_graph

graph = build_graph()

for node, edges in graph.items():
    print("\n", node, "->")
    for e in edges:
        print("   ", e)