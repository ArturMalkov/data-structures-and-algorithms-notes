"""
Traversing a data structure means systematically visiting each item stored within it.
One common use of recursion is to traverse data structures that have a naturally recursive definition.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


item1 = Node("dog")
item2 = Node("cat")
item3 = Node("rat")

item1.next = item2
item2.next = item3

# or
head = Node("Dog", Node("Cat", (Node("Rat", None))))


def traverse(head):
    # Base case
    if head is None:
        return
    # Recursive case
    print(head.data)
    traverse(head.next)


traverse(item1)
