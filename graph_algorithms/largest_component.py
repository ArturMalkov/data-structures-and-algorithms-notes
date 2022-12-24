"""
n - number of nodes
e - number of edges
Time complexity: O(e) - we're exploring through the entire graph
Space complexity: O(n) - we're going to store all nodes in a set to track visited/unvisited ones

???????????? SOLUTION DOESN'T WORK
"""


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def explore_size(graph, node, visited):
    # base case
    if node in visited:
        return 0  # to avoid excessive recursive call (to not double-count the nodes)

    visited.add(node)

    size = 1

    if graph[node]:
        for neighbor in graph[node]:
            size += explore_size(graph, neighbor, visited)

    return size


def largest_component(graph):
    visited = set()  # to avoid cycles
    longest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > longest:
            longest = size

    return longest


print(largest_component(graph))
