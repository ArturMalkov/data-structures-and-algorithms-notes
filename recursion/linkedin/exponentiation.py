"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def exp_iterative(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


def exp_iterative2(a, n):
    base = a
    for i in range(n-1):
        a *= base
    return a

# 5 ** 3
# 5 * exp_recursive(5, 2)
#     * 5 * exp_recursive(5, 1)


def exp_recursive(a, n):
    if n == 1:
        # Base case
        return a
    # Recursive case
    return a * exp_recursive(a, n-1)


assert exp_iterative(5, 3) == 125
assert exp_iterative(2, 4) == 16
assert exp_iterative(1, 19) == 1
assert exp_iterative(0, 2) == 0

assert exp_recursive(5, 3) == 125
assert exp_recursive(2, 4) == 16
assert exp_recursive(1, 19) == 1
assert exp_recursive(0, 2) == 0
