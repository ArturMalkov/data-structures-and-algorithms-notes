"""
Explores all directions evenly, visiting immediate neighbors (instead of just favoring one direction all the way through)
Uses queue
"""


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def breadth_first_print_iterative(graph, source):
    queue = [source]  # demands a queue, thus, only iterative solution is possible
    while len(queue) > 0:
        current = queue.pop()
        print(current)
        if graph[current]:
            for neighbor in graph[current]:
                queue.insert(0, neighbor)


breadth_first_print_iterative(graph, "a")
