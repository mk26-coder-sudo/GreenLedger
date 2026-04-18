from collections import deque

def bfs_proximity(graph, start):
    visited = set()
    queue = deque([(start, 0)])

    proximity = {}

    while queue:
        node, dist = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        # base distance weight
        if dist == 0:
            base = 1.0
        elif dist == 1:
            base = 0.85
        elif dist == 2:
            base = 0.65
        else:
            base = 0.5

        proximity[node] = base

        # IMPORTANT: now we use edge types
        for neighbor, weight, edge_type in graph[node]:

            if neighbor in visited:
                continue

            # edge influence
            if edge_type == "adj":
                factor = 1.0
            elif edge_type == "wind":
                factor = 1.2
            elif edge_type == "drain":
                factor = 0.9

            final = base * weight * factor

            if neighbor in proximity:
                proximity[neighbor] = max(proximity[neighbor], final)
            else:
                proximity[neighbor] = final

            queue.append((neighbor, dist + 1))

    return proximity