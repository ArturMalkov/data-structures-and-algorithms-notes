"""
a**n = a**(n-1) * a - O(N)

Shortcut for even powers:
a**n = (a**2)**(n/2) - O(log(N))
"""


def power(a: float, n: int):
    assert n >= 0
    if n == 0:
        return 1
    elif n % 2 == 1:  # for odd powers
        return power(a, n-1) * a
    else:  # for even powers
        return power(a**2, n//2)

# 2 ** 4
#
# 1
#
# power(2, 1) * 2
# ^^^
# power(2, 2) * 2
# ^^^
# power(2, 3) * 2
