"""
input:
A -> B -> C
q -> r -> s

output:
A -> q -> B -> r -> C -> s
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

q = Node("Q")
r = Node("R")

q.next = r


# Time: O(min(n, m) - n is a length of list1 and m is a length of list2
# Space: O(1) - using a fixed number of elements
def zipper_linked_lists(head1, head2):
    tail = head1  # first node in the output
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 and current2:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1

    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    return head1


print(zipper_linked_lists(a, q))


# Time: O(n)
# Space: O(n)
def zipper_linked_lists_recursively(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_linked_lists_recursively(next1, next2)
    return head1


print(zipper_linked_lists_recursively(a, q))
