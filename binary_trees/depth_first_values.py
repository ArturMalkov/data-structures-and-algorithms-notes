# Time complexity: O(n), where n is a number of nodes
# - we're going to add each node to the stack and pop it from there exactly once
# - we're not double visiting any nodes


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

# depth-first traversal (depth-first - in depth, not in width)
# a b d e c f


# uses stack data structure


def depth_first_values_iterative(root):
    stack = [root] if root else []  # emulating a stack with append() and pop() methods (end of the list is the top of the stack)
    result = []
    while len(stack) > 0:  # while there's at least one element on the stack, there is some work to be done here
        current = stack.pop()
        # print(current.value)
        result.append(current.value)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


print(depth_first_values_iterative(a))


#    a
#   / \
#  b   c
# / \   \
# d  e   f

# depth-first traversal
# a b d e c f


def depth_first_values_recursive(root):
    # base case - empty tree passed in
    if root is None:
        return []

    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)

    return [root.value, *left_values, *right_values]


print(depth_first_values_recursive(a))

# left_values = depth_first_values_recursive(b)
#               left_values = depth_first_values_recursive(d)
#                             left_values = []
#                             right_values = []
#               right_values = depth_first_values_recursive(e)
#                             right_values = []
