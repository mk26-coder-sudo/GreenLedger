from collections import deque

def bfs_proximity(graph, start):
    visited = set()
    queue = deque([(start, 0)])  # (node, distance)

    proximity = {}

    while queue:
        node, dist = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        # assign weight
        if dist == 0:
            weight = 1.0
        elif dist == 1:
            weight = 0.9
        elif dist == 2:
            weight = 0.7
        else:
            weight = 0.5

        proximity[node] = weight

        # traverse neighbors
        for neighbor, _, _ in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))

    return proximity
import heapq

def optimize_zones(graph, zones, k=3):
    heap = []

    for zone_id, zone in zones.items():
        heapq.heappush(heap, (-zone["score"], zone_id))

    selected = []
    visited = set()

    while heap and len(selected) < k:
        score, zone_id = heapq.heappop(heap)

        if zone_id in visited:
            continue

        selected.append(zone_id)
        visited.add(zone_id)

        proximity = bfs_proximity(graph, zone_id)

        for node, weight in proximity.items():
            zones[node]["score"] *= (1 - 0.3 * weight)
            heapq.heappush(heap, (-zones[node]["score"], node))

    return selected