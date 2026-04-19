import heapq
from services.bfs_service import bfs_proximity

def optimize_zones(graph, zones, k=3, total_saplings=100):

    heap = []

    # -----------------------
    # STEP 1: Build heap
    # -----------------------
    for zone_id, zone in zones.items():
        heapq.heappush(heap, (-zone["score"], zone_id))

    selected = []
    visited = set()

    # -----------------------
    # STEP 2: Select zones (FIXED LOOP)
    # -----------------------
    for _ in range(k):

        # collect mandatory zones (not yet selected)
        mandatory_zones = [
            z for z in zones
            if zones[z].get("mandatory") and z not in visited
        ]

        if mandatory_zones:
            next_zone = max(mandatory_zones, key=lambda z: zones[z]["score"])
        else:
            # pop until unused zone found
            while heap:
                _, candidate = heapq.heappop(heap)
                if candidate not in visited:
                    next_zone = candidate
                    break
            else:
                break  # no zones left

        # add to result
        selected.append(next_zone)
        visited.add(next_zone)

        # -----------------------
        # BFS impact after each pick
        # -----------------------
        proximity = bfs_proximity(graph, next_zone)

        for node, weight in proximity.items():
            if node in zones:
                zones[node]["score"] *= (1 - 0.3 * weight)

        # rebuild heap (updated scores)
        heap = []
        for z in zones:
            if z not in visited:
                heapq.heappush(heap, (-zones[z]["score"], z))

    # -----------------------
    # STEP 3: Allocation
    # -----------------------
    original_scores = {z: zones[z]["score"] for z in selected}

    allocation = {}
    saplings_left = total_saplings

    total_score = sum(original_scores.values()) + 1e-6

    for zone_id in selected:
        ratio = original_scores[zone_id] / total_score
        saplings = int(ratio * total_saplings)

        saplings = max(3, saplings)
        saplings = min(saplings, saplings_left)

        allocation[zone_id] = saplings
        saplings_left -= saplings

    return {
        "selected_zones": selected,
        "allocation": allocation,
        "saplings_left": saplings_left
    }