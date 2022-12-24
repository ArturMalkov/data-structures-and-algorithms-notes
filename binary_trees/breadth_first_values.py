# Breadth-first search is an algorithm for searching a tree data structure for a node that satisfies a given property.
# It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.
#
# Time complexity: O(n), where n is the number nodes
# we're going to add every node to the queue once, and it's going to leave the queue once
# no double adding/visiting nodes
# Space complexity: O(n) - we're adding at most all of the nodes in our queue
# Time complexity is O(n) assuming that adding and removing from the queue runs in constant time (using built-in efficient queue data structure)


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

#    a
#   / \
#  b   c
# / \   \
# d  e   f

# breadth-first traversal - breadth-first - in width, not in depth
# a b c d e f

# uses queue data structure


def breadth_first_values(root):
    if root is None:
        return []

    values = []
    queue = [root]

    while len(queue) > 0:
        current = queue.pop()
        values.append(current.value)

        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)

    return values


print(breadth_first_values(a))


# ! no straightforward way to implement breadth-first traversal recursively because breadth-first traversal needs a queue order
# any recursive code uses a stack


