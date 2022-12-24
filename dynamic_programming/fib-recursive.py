"""
Fibonacci tree - a variant of a binary tree where a tree of order n (n>1) has a left subtree of order n-1
and a right subtree of order n-2.
An order 0 Fibonacci tree has no nodes, and an order 1 tree has 1 node.
O(Fibn)
"""


def worst_fib(n):
    if n <= 1:
        return n
    return worst_fib(n-1) + worst_fib(n-2)


def best_fib(n):  # O(n)  # dynamic programming is an optimization over plain recursion.
    # best solution
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
