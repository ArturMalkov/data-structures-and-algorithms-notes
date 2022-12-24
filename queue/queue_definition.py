"""
Queue - sequential access linear data structure (unlike list (array) which is a random access data structure - when each
element can be accessed directly and in constant time)

Sequential access data structures can only be accessed in a particular order:
- each element is dependent on the others;
- may only be obtained through those other elements.

Processes collection of items if First-it First-out (FIFO) order:
- enqueue - append value to tail (right end) of queue - 'append(value)';
- dequeue - pop (returns and removes) value from head (left end) of queue - 'popLeft()';
- check if empty

Queue requires efficient append() and remove() O(1) operations.

Use cases in programming:
- job scheduling (the process through which the computer decides which task to complete for the user and when);
- asynchronous programming.

Use cases in real world:
- printer queueing.
"""


class Node:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail


class QueueLinkedList:
    def __init__(self, *start):
        self.head = None
        self.tail = None
        for _ in start:
            self.append(_)

    def append(self, value):
        """Adds value to the end of queue. O(1) operation."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self):
        """Determines whether queue is empty"""
        return self.head is None

    def pop(self):
        """Removes first value from queue. O(1) operation."""
        if self.head is None:
            raise Exception("Queue is empty.")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def __iter__(self):
        """Iterator of value in queue"""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        """String representation of queue"""
        return f""


if __name__ == "__main__":
    queue = QueueLinkedList(1, 2, 3)
    for _ in queue:
        print(_)

    print(queue.pop())
    print("------")

    for _ in queue:
        print(_)
