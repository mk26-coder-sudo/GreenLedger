from data.zones import zones

def build_graph():
    graph = {}

    # initialize nodes
    for zone_id in zones:
        graph[zone_id] = []

    # ----------------------------
    # 1. ADJACENCY EDGES
    # ----------------------------
    for zone_id, data in zones.items():
        for neighbor in data["neighbors"]:
            graph[zone_id].append((neighbor, 1.0, "adj"))

            # reverse edge (avoid duplicates)
            if zone_id not in [n for n, _, _ in graph[neighbor]]:
                graph[neighbor].append((zone_id, 1.0, "adj"))

    # ----------------------------
    # 2. WIND EDGES
    # ----------------------------
    for zone_id, data in zones.items():
        for wind_target in data.get("wind_out", []):
            graph[zone_id].append((wind_target, 0.7, "wind"))

    # ----------------------------
    # 3. DRAIN EDGES
    # ----------------------------
    for zone_id, data in zones.items():
        for drain_target in data.get("drain_to", []):
            graph[zone_id].append((drain_target, 0.6, "drain"))

    return graph