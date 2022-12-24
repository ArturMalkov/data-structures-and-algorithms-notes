"""
Return True or False depending on whether a target value is present in a linked list or not.
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
# Space: O(1) - we're using a constant number of variables
def linked_list_find(head, target):
    current = head
    while current:  # is not None
        if current.value == target:
            return True
        current = current.next
    return False


print(linked_list_find(a, "G"))
print(linked_list_find(a, "D"))


# Time: O(n)
# Space: O(n) - because of calls on call stack
def linked_list_find_recursively(head, target):
    if head is None:  # the end of linked list or an empty linked list
        return False
    if head.value == target:
        return True
    return linked_list_find_recursively(head.next, target)


print(linked_list_find(a, "G"))
print(linked_list_find(a, "D"))
