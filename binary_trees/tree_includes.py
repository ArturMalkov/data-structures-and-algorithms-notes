# breadth-first iterative approach
# Time complexity: O(n) - each node enters and leaves the queue only once (considering we use efficient built-in queue -
# with constant time add/remove operations)
# Space complexity: O(n) - we store each node in the queue only once
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def tree_includes_iterative(root, target):
    if root is None:
        return False

    queue = [root]

    while len(queue) > 0:
        current = queue.pop()
        if current.value == target:
            return True

        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)

    return False


print(tree_includes_iterative(a, "z"))


# depth-first recursive approach


def tree_includes_recursive(root, target):
    # base case 1 - affirmative
    if root is None:
        return False
    # base case 2 - negatory
    if root.value == target:
        return True
    # logical OR - False or False = False; False or True = True
    return tree_includes_recursive(root.left, target) or tree_includes_recursive(root.right, target)
