class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a1 = Node(2)
a2 = Node(4)
a3 = Node(8)
a4 = Node(11)
a5 = Node(23)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

b1 = Node(3)
b2 = Node(4)
b3 = Node(10)
b4 = Node(15)
b5 = Node(22)

b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5


def merge_linked_lists(A, B):  # where A and B are head nodes of two linked lists
    # base case
    if A is None:
        return B
    if B is None:
        return A

    # recursive case
    if A.value < B.value:
        A.next = merge_linked_lists(A.next, B)
        return A
    else:
        B.next = merge_linked_lists(A, B.next)
        return B


result = merge_linked_lists(a1, b1)

while result:
    print(result.value)
    result = result.next
