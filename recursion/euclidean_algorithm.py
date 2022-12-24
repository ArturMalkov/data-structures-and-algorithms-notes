"""
Find GCD - greatest common divisor
Euclidean algorithm:
a --------------------
b ---------XXXXXXXXXXX - this difference is also divisible by GCD
GCD(a, b) = GCD(a-b, b), provided that a > b OR GCD(a, b) = GCD(b, a % b)
GCD(a, b) = a, provided that a = b
"""


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:  # a < b
        return gcd(a, b-a)


def better_gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def better_shorter_gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
