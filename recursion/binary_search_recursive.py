# works for sorted lists
def binary_search(A, left, right, x):  # A is a list, x is a search value, left is on the left of the value, etc.
    if left > right:
        return -1
    mid = (left + right) // 2
    if x == A[mid]:
        return mid
    if x < A[mid]:
        return binary_search(A, left, mid-1, x)
    return binary_search(A, mid, right, x)  # if x > A[mid]


print(binary_search([-1, 0, 1, 2, 3, 4, 7, 9, 10], 0, 9, 10))  # leftmost elem's index is 0, rightmost elem's index is 9
