from data.zones import zones

def build_graph():
    graph = {}

    # initialize all nodes
    for zone_id in zones:
        graph[zone_id] = []

    # add edges
    for zone_id, data in zones.items():
        for neighbor in data["neighbors"]:
            
            # forward edge
            graph[zone_id].append((neighbor, 1.0, "adj"))

            # reverse edge (only if not already added)
            if zone_id not in [n for n, _, _ in graph[neighbor]]:
                graph[neighbor].append((zone_id, 1.0, "adj"))

    return graph