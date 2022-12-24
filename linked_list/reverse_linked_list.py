"""
Reverse the order of the nodes in linked list and return its new head.
A -> B -> C -> None
C -> B -> A -> None
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
# Space: O(1) - constant number of variables (3 pointers - "prev", "current" and "next")
def reverse_linked_list(head):
    prev = None  # A's next will need to point to None after reversal
    current = head
    while current is not None:
        next = current.next  # None <- A    B -> C -> None
        current.next = prev  # prev   cur  next
        prev = current
        current = next
    return prev


print(reverse_linked_list(a))


# Time: O(n)
# Space: O(n)
def reverse_linked_list_recursively(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_linked_list_recursively(next, head)


print(reverse_linked_list_recursively(a))


def new_recursive_reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    p = new_recursive_reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    # p will be propagated down the call stack to the original caller to be the new head node
    return p
