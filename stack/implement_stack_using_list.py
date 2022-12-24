class Stack:
    def __init__(self):
        """Use list as storage for a stack"""
        self.stack = []

    def is_empty(self):  # O(1)
        """Determines whether stack is empty"""
        return len(self.stack) == 0

    def push(self, value):  # O(1) - amortized cost
        """Pushes value onto the stack"""
        self.stack.append(value)

    def pop(self):  # O(1) - amortized cost
        """Removes topmost item from stack and returns it"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def __repr__(self):
        return f"stack: {str(self.stack)}"
