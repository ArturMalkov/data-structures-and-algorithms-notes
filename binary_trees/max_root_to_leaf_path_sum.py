# Time complexity: O(n) - make a call for every node in the tree
# Space complexity: O(n) - due to a call stack


def max_path_sum(root):
    if root is None:
        return -10**9  # or negative infinity
    # base case - we reached a leaf node
    if root.left is None and root.right is None:
        return root.value

    max_child_path_sum = max(max_path_sum(root.left), max_path_sum(root.right))
    return root.value + max_child_path_sum
