"""
Traversing through a linked list - touching and processing every single node in a linked list.
We only need a reference to its head node for this.
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

# A -> B -> C -> D -> None
# cur


def print_linked_list(head):  # Time: O(n) (iterating through every node once)
    current = head  # pointer starts at the head node
    while current:  # ! not current.next because in this case we'll lose the last node (its next will be None)
        print(current.value)
        current = current.next  # moving pointer with each iteration


print_linked_list(a)


# A -> B -> C -> D -> None
# head
# A is a head of its linked list: A -> B -> C -> D -> None
# B is a head of its own linked list: B -> C -> D -> None
# etc. - which is why we call the parameter "head" below
def print_linked_list_recursively(head):
    if head is None:
        return
    print(head.value)
    print_linked_list_recursively(head.next)


print_linked_list_recursively(a)
