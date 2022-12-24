class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


# breadth-first traversal
def tree_sum(root):
    if root is None:
        return 0

    total_sum = 0
    queue = [root]

    while len(queue) > 0:
        current = queue.pop()
        total_sum += current.value

        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)

    return total_sum


print(tree_sum(a))


# depth-first traversal
# Time complexity: O(n) - one call per every single node
# Space complexity: O(n) - call stack
def tree_sum_recursive(root):
    if root is None:
        return 0  # null nodes will return 0 down the call stack / empty tree
    return root.value + tree_sum_recursive(root.left) + tree_sum_recursive(root.right)
