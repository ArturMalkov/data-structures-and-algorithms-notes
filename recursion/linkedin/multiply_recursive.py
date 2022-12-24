"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
# 4 * 3
# 3 + multiply_recursive(3, 3)
#    + 3 + multiply_recursive(2, 3)
#          + 3 + multiply_recursive(1, 3)


def multiply_recursive(n, a):
    if n == 1:
        # Base case
        return a
    # Recursive case
    return a + multiply_recursive(n-1, a)


assert multiply_recursive(5, 4) == 20  # 5 is the multiplier, 4 is the multiplicand
assert multiply_recursive(5, -4) == -20  # 5 is the multiplier, -4 is the multiplicand
assert multiply_recursive(1, 4) == 4  # 1 is the multiplier, 4 is the multiplicand
assert multiply_recursive(7, 8) == 56  # 7 is the multiplier, 8 is the multiplicand
