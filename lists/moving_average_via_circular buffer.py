"""
Implementation of a moving average by extending CircularBuffer
"""

from implement_circular_buffer import CircularBuffer


class MovingAverage(CircularBuffer):
    def __init__(self, size):
        """Stores buffer in a given storage"""
        super().__init__(size)
        self.total = 0

    def get_average(self):
        """Returns moving average (0 if no elements)"""
        if self.count == 0:
            return 0
        return self.total / self.count

    def remove(self):
        """Removes oldest value from non-empty buffer"""
        removed = super().remove()
        self.total -= removed
        return removed

    def add(self, value):
        """Adds value to buffer, overwrite as needed"""
        if self.is_full():
            delta = -self.buffer[self.low]
        else:
            delta = 0
        delta += value
        self.total += delta
        super().add(value)

    def __repr__(self):
        """String representation of moving average"""
        if self.is_empty():
            return f"ma: []"
        return f"ma: [{','.join(map(str, self))}]"
