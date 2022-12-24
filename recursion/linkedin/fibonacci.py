"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# Time complexity: O(2^n)
# Space complexity: O(n) - number of stack frames in the call stack at any given moment
def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_iterative(6))
print(fibonacci_recursive(6))
