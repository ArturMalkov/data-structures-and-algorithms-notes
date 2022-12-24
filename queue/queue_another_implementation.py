"""
Enqueue and dequeue on the left end of a linked list both have O(1) complexity, while enqueue and dequeue on the right end
of a linked list have O(1) and O(n) complexity correspondingly
=> we will enqueue from the right end of a linked list and dequeue from the left end of a linked list (both are O(1)).
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        self.first = self.last = Node(value)
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        target = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            target.next = None
        self.length -= 1
        return target

    def print_queue(self):
        current = self.first

        while current:
            print(current.value)
            current = current.next


my_queue = Queue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.print_queue()

print("*" * 5)
my_queue.dequeue()
my_queue.print_queue()
print("*" * 5)
my_queue.dequeue()
my_queue.print_queue()
print("*" * 5)
my_queue.dequeue()
my_queue.print_queue()
print("*" * 5)
