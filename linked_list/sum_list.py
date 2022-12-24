"""
Return the total sum of values of nodes in a linked list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)

a.next = b
b.next = c
c.next = d


# Time: O(n)
# Space: O(1) - need to only maintain "current" and "sum" variables
def sum_linked_list(head):
    sum = 0
    current = head
    while current:
        sum += current.value
        current = current.next
    return sum


print(sum_linked_list(a))


# Time: O(n)
# Space: O(n) - because of the call stack (at the end, we'll have n calls on the call stack)
def sum_linked_list_recursively(head):
    if head is None:
        return 0
    return head.value + sum_linked_list_recursively(head.next)  # + sum of the remaining nodes


print(sum_linked_list_recursively(a))
