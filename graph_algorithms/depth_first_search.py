def depth_first_search(node: Node, visited: set, goal: int) -> bool:  # goal is a node we're looking for
    # base case 1 - smallest thing we can pass in - no way we could find a goal
    if node is None:
        return False

    # base case 2 - we've actually found the node
    if node.value == goal:
        return True

    for neighbor in node.get_neighbors():
        if neighbor in visited:  # to avoid cycles (which can happen in graphs), we want to keep a set of visited values
            continue  # we never want to visit the same node more than once
        visited.add(neighbor)
        is_found = depth_first_search(neighbor, visited, goal)

        if is_found:
            return True
    # last base case - we've traversed through all the neighbors and haven't found the goal value
    return False
