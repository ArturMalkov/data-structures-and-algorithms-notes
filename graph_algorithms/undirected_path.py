"""
n - number of nodes
e - number of edges
Time complexity: O(e)
Space complexity: O(n) - number of visited nodes added to stack/queue
"""
from pprint import pprint

# every pair in the edge list represents a connection between two nodes
edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]


# convert edge list to adjacency list - to facilitate classic traversal through it
def build_graph(edges):
    graph = {}
    for edge in edges:
        for neighbor in edge:
            if neighbor not in graph:
                graph[neighbor] = [elem for elem in edge if elem != neighbor]
            else:
                graph[neighbor] += [elem for elem in edge if elem != neighbor]

    return graph


pprint(build_graph(edges))


def has_path_iterative(graph, source, dest):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop()
        if current == dest:
            return True
        if graph[current]:
            for neighbor in graph[current]:
                queue.insert(0, neighbor)
    return False


def has_path_recursive(graph, source, dest, visited):
    if source == dest:
        return True
    if source in visited:  # to avoid cycles and, thus, infinite recursion
        return False
    else:
        visited.add(source)

    for neighbor in graph[source]:
        if has_path_recursive(graph, neighbor, dest, visited):
            return True

    return False


def undirected_path(edges, node_a, node_b):
    graph = build_graph(edges)
    return has_path_recursive(graph, node_a, node_b, visited=set())


print(undirected_path(edges, "i", "k"))
