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
    # STEP 2: Select zones
    # -----------------------
    while heap and len(selected) < k:
        score, zone_id = heapq.heappop(heap)

        if zone_id in visited:
            continue

        visited.add(zone_id)
        selected.append(zone_id)

    # -----------------------
    # STEP 3: SNAPSHOT SCORES
    # -----------------------
    original_scores = {z: zones[z]["score"] for z in zones}

    sorted_selected = sorted(
        selected,
        key=lambda z: original_scores[z],
        reverse=True
    )

    allocation = {}
    saplings_left = total_saplings

    total_score = sum(original_scores[z] for z in sorted_selected) + 1e-6

    # -----------------------
    # STEP 4: Allocate saplings
    # -----------------------
    for zone_id in sorted_selected:

        if saplings_left <= 0:
            allocation[zone_id] = 0
            continue

        ratio = original_scores[zone_id] / total_score
        saplings = int(ratio * total_saplings)

        saplings = max(3, saplings)
        saplings = min(saplings, saplings_left)

        allocation[zone_id] = saplings
        saplings_left -= saplings

    # -----------------------
    # STEP 5: BFS impact
    # -----------------------
    for zone_id in selected:
        proximity = bfs_proximity(graph, zone_id)

        for node, weight in proximity.items():
            if node in zones:
                zones[node]["score"] *= (1 - 0.3 * weight)

    return {
        "selected_zones": selected,
        "allocation": allocation,
        "saplings_left": saplings_left
    }