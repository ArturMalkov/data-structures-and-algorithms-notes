"""
Stack - linear (vertical) and sequential access data structure (unlike list which is a linear and random access data structure -
when each element can be accessed directly and in constant time)

Sequential access data structures can only be accessed in a particular order:
- each element is dependent on the others;
- may only be obtained through those other elements.

Processes collection of values in Last-in First-out (LIFO) order:
- push value onto the stack - 'push(value)';
- pop and retrieve most recently added value - 'pop()';
- check if empty.

You'll never want to sort the stack - it's always structured the way it was created:
- you push some items onto the stack, and then you pop them out in reverse order.

Use cases in programming:
- Python virtual machine is a stack-based one (call stack, stack frames);
- recursion (used for traversing certain data structures, etc.).

Use cases in real world:
- undo/redo buttons;
- back-paging buttons (return the latest-visited page).
"""
# implement a stack using a linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.top is None:  # if self.height == 0
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.top is None:  # if self.height == 0
            return None

        target = self.top
        self.top = self.top.next
        target.next = None
        self.height -= 1
        return target

    def print_stack(self):
        current = self.top

        while current:
            print(current.value)
            current = current.next


my_stack = Stack(2)
my_stack.push(1)
my_stack.print_stack()

my_stack.pop()
my_stack.print_stack()
