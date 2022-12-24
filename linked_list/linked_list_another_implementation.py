class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = self.tail = Node(value)
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev = self.get(index-1)

        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def pop(self):
        """O(n) operation since we need to iterate to the element before the last one unlike in doubly-linked lists which have 'prev' pointers"""
        if self.head is None:
            return None

        temp = prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None

        return temp

    def pop_first(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if self.head is None:
            return None

        if index < 0 or index >= self.length:
            return None

        current = self.head
        for _ in range(index):
            current = current.next

        return current

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None

        target = self.get(index)
        if target:
            target.value = value
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        prev = self.get(index-1)
        target = prev.next  # more efficient than self.get(index) which is O(n) operation

        prev.next = target.next
        target.next = None
        self.length -= 1
        return target

    def reverse(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        current = temp

        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after

        return self.head

    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)

my_linked_list.prepend(0)

my_linked_list.print_list()
#
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())

# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())

print(my_linked_list.get(1))
my_linked_list.set_value(1, 100)

my_linked_list.print_list()
my_linked_list.insert(1, 200)

my_linked_list.print_list()

my_linked_list.remove(2)
my_linked_list.print_list()

my_linked_list.reverse()
my_linked_list.print_list()
