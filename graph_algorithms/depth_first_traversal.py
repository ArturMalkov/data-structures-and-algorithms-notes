"""
You're exploring one direction as fas as possible before switching directions.
Uses stack
"""

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def depth_first_print_iterative(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        if graph[current]:
            for neighbor in graph[current]:
                stack.append(neighbor)


depth_first_print_iterative(graph, "a")


print("-------------")


def depth_first_print_recursive(graph, source):
    print(source)
    if graph[source]:
        for neighbor in graph[source]:
            depth_first_print_recursive(graph, neighbor)


depth_first_print_recursive(graph, "a")
