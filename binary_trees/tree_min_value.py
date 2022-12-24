class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def tree_min_value_iterative_queue(root):
    if root is None:
        return None

    min_val = root.value
    queue = [root]
    while len(queue) > 0:
        current = queue.pop()  # if we use a non built-in (efficient) queue, it'll be O(n**2) solution - each pop operation is O(n)
        if current.value < min_val:
            min_val = current.value

        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)

    return min_val


print(tree_min_value_iterative_queue(a))


# Time complexity: O(n) - number of recursive calls
# Space complexity: O(n)
def tree_min_value_iterative_stack(root):
    min_value = 10 ** 9
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if current.value < min_value:
            min_value = current.value

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return min_value


print(tree_min_value_iterative_stack(a))


#    5
#   / \
# 11   3
# / \   \
# 4  5   12

def tree_min_value_recursive(root):
    if root is None:
        return 10 ** 10
    left_min = tree_min_value_recursive(root.left)
    right_min = tree_min_value_recursive(root.right)
    return min(root.value, left_min, right_min)


print(tree_min_value_recursive(a))
