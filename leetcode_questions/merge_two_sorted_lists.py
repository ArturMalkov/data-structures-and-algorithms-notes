"""
21 leetcode problem
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


a = Node(1)
b = Node(2)
c = Node(4)
a.next = b
b.next = c

d = Node(1)
e = Node(3)
f = Node(4)
d.next = e
e.next = f


def print_linked_list(node: Node):
    while node:
        print(node.value)
        node = node.next


print_linked_list(a)
print_linked_list(d)
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


def merge_sorted_linked_lists(node1: Node, node2: Node):
    dummy_node = Node(0)
    tail = dummy_node

    while node1 and node2:
        if node1.value <= node2.value:
            tail.next = node1
            node1 = node1.next
            # next_node1 = node1.next
            # node1.next = node2
            # node1 = next_node1
        else:
            tail.next = node2
            node2 = node2.next
            # next_node2 = node2.next
            # node2.next = node1
            # node2 = next_node2
        tail = tail.next

    if node1:
        tail.next = node1
    if node2:
        tail.next = node2
    # if node1:
    #     node2.next = node1
    # if node2:
    #     node1.next = node2
    return dummy_node.next


print("-------")
merge_sorted_linked_lists(a, d)
print_linked_list(a)
