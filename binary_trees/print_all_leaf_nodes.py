def print_leaves(root):
    # base case
    if root is None:
        return

    # Checks if a given node is a leaf (which has no children (to the left or to the right))
    if root.left is None and root.right is None:
        print(root.value + ", ")
        return

    # recursive case - to the left sub-half of the tree
    if root.left is not None:
        print_leaves(root.left)
    # recursive case - to the right sub-half of the tree
    if root.right is not None:
        print_leaves(root.right)
