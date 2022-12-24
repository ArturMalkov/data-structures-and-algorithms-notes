"""
Return a node's value at a particular index.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d


# Time: O(n)
# Space: O(1) - tracking the same number of variables ("current" and "count")
def get_node_value(head, idx):
    current = head
    count = 0
    while current:
        if count == idx:
            return current.value
        count += 1
        current = current.next
    return None  # if an index is too large


print(get_node_value(a, 1))


# Time: O(n)
# Space: O(n) - call stack
def get_node_value_recursively(head, idx):
    if head is None:  # if index out of range or a list is empty
        return None
    if idx == 0:
        return head.value
    return get_node_value_recursively(head.next, idx-1)


print(get_node_value_recursively(a, 3))
