"""
Return an array of the values (in order) of all nodes from the linked list.
values = [A, B, C, D]
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


# Time: O(n) (iterating through every node once)
# Space: O(n) - the size of the output array
def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


print(linked_list_values(a))


# split recursive option
# Time: O(n) (iterating through every node once)
# Space: O(n) - the size of the output array
def linked_list_values_recursive(head):
    values = []
    add_values(head, values)
    return values


def add_values(head, values):
    if head is None:
        return
    values.append(head.value)
    add_values(head.next, values)


print(linked_list_values_recursive(a))


# combined recursive option - mutable default argument is needed for recursive calls to mutate the same list
# i.e. values are added to the same array
def combined_recursive_option(head, values=[]):  # new list is not created with each recursive call!
    if head is None:
        return
    values.append(head.value)
    combined_recursive_option(head.next, values)
    return values


print(combined_recursive_option(a))
