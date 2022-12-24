"""
edges = [
    [w, x],
    [x, y],
    [z, y],
    [z, v],
    [w, v]
]

start: w
end: z

Path length - number of edges within the path.
"""

edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"]
]


# breadth-first approach is more useful here - linear complexity
def shortest_path(edges, node_a, node_b):
    graph = build_graph(edges)
    visited = {node_a}
    queue = [[node_a, 0]]  # node_a is 0 edges away from itself

    while len(queue) > 0:
        [node, distance] = queue.pop()

        if node == node_b:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:  # to avoid cycles
                visited.add(neighbor)
                queue.insert(0, [neighbor, distance + 1])

    return -1  # if there's no path between node_a and node_b, return -1


def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


print(build_graph(edges))
print(shortest_path(edges, "w", "z"))
