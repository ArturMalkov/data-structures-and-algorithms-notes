"""
n - number of nodes
e - number of edges

Time complexity: O(e)
Space complexity: O(n)
"""

graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}


def explore(graph, current, visited=set()):
    if current in visited:  # to prevent cycles
        return False
    else:
        visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True  # after all the neighbors have been explored


def connected_component_count(graph):
    count = 0

    for node in graph:
        if explore(graph, node):  # if not is already explored, this will return False
            count += 1

    return count


print(connected_component_count(graph))
