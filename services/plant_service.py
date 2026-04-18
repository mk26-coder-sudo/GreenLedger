from copy import deepcopy
from services.bfs_service import bfs_proximity

def plant_trees(graph, zones, allocation):

    before_state = deepcopy(zones)

    # -------------------------
    # APPLY PLANTING
    # -------------------------
    for zone_id, saplings in allocation.items():

        try:
            zone_id = int(zone_id)
        except:
            continue

        if zone_id not in zones:
            continue

        # DIRECT IMPACT
        zones[zone_id]["score"] -= saplings * 0.1
        zones[zone_id]["score"] = max(0, zones[zone_id]["score"])

        # BFS SPREAD
        proximity = bfs_proximity(graph, zone_id)

        for node, weight in proximity.items():

            if node not in zones or node == zone_id:
                continue

            zones[node]["score"] -= saplings * 0.05 * weight
            zones[node]["score"] = max(0, zones[node]["score"])

    # -------------------------
    # CALCULATE IMPACT (THIS WAS THE ISSUE AREA)
    # -------------------------
    diff = {}   

    for zone_id in zones:
        before_score = before_state[zone_id]["score"]
        after_score = zones[zone_id]["score"]

        diff[zone_id] = round(before_score - after_score, 2)

    # -------------------------
    # RETURN
    # -------------------------
    return {
        "before": before_state,
        "after": deepcopy(zones),
        "impact": diff   
    }