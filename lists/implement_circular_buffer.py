class CircularBuffer:
    def __init__(self, size):
        """Initializing fixed-size buffer"""
        self.size = size
        self.buffer = [None] * size
        self.low = 0
        self.high = 0
        self.count = 0

    def is_empty(self):  # O(1)
        return self.count == 0

    def is_full(self):  # O(1)
        return self.count == self.size

    def add(self, value):  # O(1)
        if not self.is_full():
            self.count += 1
        else:
            self.low = (self.low + 1) % self.size
        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size

    def remove(self):  # O(1)
        if self.is_empty():
            raise Exception("Buffer is empty")
        value = self.buffer[self.low]
        self.low = (self.low + 1) % self.size
        self.count -= 1
        return value

    def __iter__(self):  # O(n)
        idx = self.low
        num = self.count
        while num > 0:
            yield self.buffer[idx]
            idx = (idx + 1) % self.size
            num -= 1

    def __repr__(self):
        if self.is_empty():
            return "cb: []"
        return f"cb: [{'.'.join(map(str, self))}]"


if __name__ == "__main__":
    cb = CircularBuffer(4)
    print(cb)
    cb.add(5)
    print(cb)
