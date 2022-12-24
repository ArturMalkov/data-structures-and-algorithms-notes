"""
Doubly-Linked list - sequential access data structure.

Able to traverse both forwards and backwards using 'next' and 'previous' pointers.

Use cases:
the back and forth functionality lends itself to be implemented in a lot of stack-like functionality:
    - undo/redo functions;
    - browser caches allowing you to go back and forth on webpages.

Often used to implement a deque.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        self.head = self.tail = Node(value)
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:  # if self.length == 0
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        """O(1) operation (unlike in linked lists) since we have 'prev' pointer and do not have to iterate through the list"""
        if self.head is None:  # if self.length == 0
            return None
        target = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:  # if self.length >= 2
            self.tail = self.tail.prev
            self.tail.next = None
            target.prev = None
        self.length -= 1
        return target

    def pop_first(self):
        if self.head is None:  # if self.length == 0
            return None
        target = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            target.next = None
        self.length -= 1
        return target

    def get(self, index):
        """Optimized approach for doubly-linked lists (the previous approach for a singly-linked list still works)"""
        if index < 0 or index >= self.length:
            return None

        if index < self.length / 2:  # if the item is in the first half of the list
            target = self.head
            for _ in range(index):
                target = target.next
        else:  # if the item is in the second half of the list
            target = self.tail
            for _ in range(self.length-1, index, -1):
                target = target.prev
        return target

    def set_value(self, index, value):
        target = self.get(index)
        if target:
            target.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        before = self.get(index-1)
        target = before.next
        after = target.next

        before.next = after
        after.prev = before
        target.prev = None
        target.next = None

        # another approach
        # target = self.get(index)
        # target.prev.next = target.next
        # target.next.prev = target.prev
        # target.prev = None
        # target.next = None

        self.length -= 1
        return True

    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()

# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())

my_doubly_linked_list.print_list()
my_doubly_linked_list.prepend(100)
my_doubly_linked_list.print_list()
my_doubly_linked_list.append(1000)
# my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print_list()

print(my_doubly_linked_list.get(1))
print(my_doubly_linked_list.get(2))

my_doubly_linked_list.set_value(3, 5)
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(2, 7)
my_doubly_linked_list.print_list()

my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()
