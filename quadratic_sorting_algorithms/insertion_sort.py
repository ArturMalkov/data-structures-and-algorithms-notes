"""
Inserting new elements to the already sorted part of the list

Worst case: O(n**2) - nested loops
Best case: O(n) - we already have (almost) sorted data
"""


def insertion_sort(A):
    for top in range(1, len(A)):  # "top" is an element being inserted (starting from index 1 - index 0 already exists (initial list of 1 element))
        k = top
        while k > 0 and A[k-1] > A[k]:  # k > 0 - i.e. while there are any elements on the left to be checked (i.e. while we are not in the leftmost position)
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1  # moving from right (newly inserted element) to left
    return A


print(insertion_sort([5, 3, 3, 2, 1, 0, 5, 7, 1, 9]))


def insertion_sort_reversed(some_list):  # 4, 2, 5, 1, 3
    for top in range(1, len(some_list)):
        i = top
        while i > 0 and some_list[i] > some_list[i-1]:
            some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
            i -= 1
    return some_list


print(insertion_sort_reversed([4, 5, 2, 1, 5, 7, 4, 2, 9, 9]))


def insertion_sort_best(some_list):
    for i in range(1, len(some_list)):
        for j in range(i, 0, -1):
            if some_list[j] < some_list[j-1]:
                some_list[j], some_list[j-1] = some_list[j-1], some_list[j]
            else:
                break
    return some_list


print(insertion_sort_best([4, 5, 2, 1, 5, 7, 4, 2, 9, 9]))
