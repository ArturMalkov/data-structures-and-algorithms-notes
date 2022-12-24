"""
Linked list - sequential access linear (elements are linked one after another) and pointer-based data structure.
Linked List is an ordered data structure that consists of nodes pointing to each other (widely used in Pascal, C/C++).
Last node's (tail) next is None.
First node is a head (at position 0).
Node is just a container for some data.

Sequential access data structures can only be accessed in a particular order:
- each element is dependent on the others;
- may only be obtained through those other elements.

Comparison to array (list):
- all elements of an array are stored next to each other in memory (contiguous structure) which impacts runtime of
different operations
a) Insertion in lists: need to shift all elements on the right by index 1 one by one - costly and slow operation - O(n).
- worst case - inserting at index 0 (the same goes for removing values from a list);
b) Insertion (prepend/append) in linked lists: no need to perform shifting of all elements on the right:
we just reset the pointer of the previous node to the new node and the pointer of the new node to the next node -
thus, need to change only 2 pointers - O(1) operation.
Insertion of a new value after a particular node - we need to iterate through a linked list to get to a particular place where
we want to insert a new node - thus, O(n) operation.
Remove target/last value from linked list: O(n) operation (we must iterate through a linked list to get to a particular node/pointer).
Removing the first node (head) from a linked list is O(1) operation while for lists it's O(n) because we'll need to shift all the indexes to the left.
c) accessing a particular node is O(n) since linked list is a sequential access data structure (unlike lists the access
in which (i.e. using indexing) is O(1) operation - lists (arrays) are random access data structures; lists are contiguous
data structures with elements stored next to each other in memory, which is why lists have indexes - and we can access those
indexes O(1) since we can map each one of those indexes to a specific address in memory)

See the LinkedList implementation of a queue in "queue" directory

Linked lists are used to avoid having a single contiguous block of memory being allocated and all the information being stored there
(nodes of a linked list are spread all over the place).

Use cases in programming:
- linked lists can be used to make stacks, queues, hash tables (deal with collisions) etc.
"""


class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail


class LinkedList:
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        """Adds value to the front of the list. O(1) operation."""
        self.head = LinkedNode(value, self.head)

    def remove(self, value):
        # if self.head is None:
        #     raise Exception("Empty list.")
        current = self.head
        prev = None

        while current:
            if current.value == value:
                if prev is None:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next
        return False

    def pop(self):
        """Removes first value from list."""
        if self.head is None:
            raise Exception("Empty list.")
        value = self.head.value
        self.head = self.head.next
        return value

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        values = []
        current = self.head

        while current:
            values.append(str(current.value))
            current = current.next

        return "->".join(values)


if __name__ == "__main__":
    a = LinkedList()
    a.prepend(1)
    a.prepend(2)
    a.prepend(3)
    a.prepend(4)
    a.prepend(5)
    # for _ in a:
    #     print(_)

    a.remove(3)

    for _ in a:
        print(_)

    print(a)
