"""
Requirement: for binary search to be performed, list must be sorted.
Left boundary - on the left of the target
Right boundary - on the right of the target

Speed complexity - O(log2N) (as opposed to linear search in unsorted lists which is O(n))
"""


def left_bound(A, key):  # A is a list, key is a value to be found
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right







