"""
Indicate whether we can travel from the source node to the destination node (i.e. path between those two nodes)
Time complexity: O(e) - where "e" is the number of edges - we need to travel through every single edge of the graph
Space complexity: O(n) - where "n" is the number of nodes

if "n" is the number of nodes, then number of edges is n**2, thus time complexity is O(n**2)
"""

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def has_path_depth_first_iterative(graph: dict, source: str, dest: str) -> bool:
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        if current == dest:
            return True
        if graph[current]:
            for neighbor in graph[current]:
                stack.append(neighbor)
    return False


def has_path_depth_first_recursive(graph, source, dest) -> bool:
    if source == dest:
        return True
    if graph[source]:
        for neighbor in graph[source]:
            if has_path_depth_first_recursive(graph, neighbor, dest):
                return True
    return False


def has_path_breadth_first(graph, source, dest) -> bool:  # breadth-first approach can only be iterative since it's based on a queue
    queue = [source]
    while len(queue) > 0:
        current = queue.pop()
        if current == dest:
            return True
        if graph[current]:
            for neighbor in graph[current]:
                queue.insert(0, neighbor)
    return False
