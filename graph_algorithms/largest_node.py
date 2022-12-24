graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def largest_node(graph):
    visited = set()
    max_value = -10 ** 11

    for node in graph:
        queue = [node]

        while len(queue) > 0:
            current = queue.pop()
            if current in visited:
                continue
            else:
                visited.add(current)
            if current > max_value:
                max_value = current

            if graph[current]:
                for neighbor in graph[current]:
                    queue.insert(0, neighbor)

    return max_value


print(largest_node(graph))
