def leaf_nodes_sum_bfs(node):
    result = 0
    queue = [node]

    while queue:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        if not current.left and not current.right:
            result += current.value

    return result


# another approach
def leaf_nodes_sum_dfs(node):
    result = []

    def traverse(current_node):
        if current_node.left:
            traverse(current_node.left)
        if current_node.right:
            traverse(current_node.right)
        if not current_node.left and not current_node.right:
            result.append(current_node.value)

    traverse(node)
    return sum(result)


# another approach
def leaf_nodes_sum_recursive(node, results=[]):
    if node is None:
        return

    if node.left is None and node.right is None:
        results.append(node.value)

    leaf_nodes_sum_recursive(node.left)
    leaf_nodes_sum_recursive(node.right)
    return sum(results)
