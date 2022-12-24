"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import inspect  # to keep track of the stack size


def factorial(n):
    print("Non tail optimised stack size: ", len(inspect.stack(0)))
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def tail_factorial_attempt(n, accumulator=1):  # emulation of tail call optimization from other languages
    print("Attempted tail optimised stack size: ", len(inspect.stack(0)))
    if n == 0:
        return accumulator  # accumulator keeps track of our result
    else:
        return tail_factorial_attempt(n - 1, accumulator * n)  # !returning recursive call only (unlike rec_call * n above)


if __name__ == "__main__":
    print(factorial(5))
    print(tail_factorial_attempt(5))
