"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import time
from functools import lru_cache


def fib(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


@lru_cache
def fib_lru(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


# Manual caching using a dictionary (key is the argument to a function, value is the return value).
# Time complexity: O(n)
# Space complexity: O(n)
def fib_cache(n, cache=None):
    if not cache:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    result = fib_cache(n - 1, cache) + fib_cache(n - 2, cache)
    cache[n] = result
    return result


n = 900

start = time.perf_counter()
fib(n)
end = time.perf_counter()
print("Plain recursive version. Seconds taken: {:.7f}".format(end - start))
#
# start = time.perf_counter()
# fib_lru(n)
# end = time.perf_counter()
# print("lru cache version. Seconds taken: {:.7f}".format(end - start))
#
# start = time.perf_counter()
# fib_cache(n)
# end = time.perf_counter()
# print("Manual cache version. Seconds taken: {:.7f}".format(end - start))
