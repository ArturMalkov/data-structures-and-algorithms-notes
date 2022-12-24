"""
Sorting is stable if it maintains the relative order of records with equal keys (i.e. values).

Space complexity: O(n), where 'n' is the number of newly created lists of length 1 (we recursively divide the initial list)
(we're not sorting in-place like in previous algorithms)
Time complexity: O(n log n) - breaking the initial list apart is O(logN), putting it back together is O(n)
"""


# merging (already) sorted lists
# A -------- with index i
# B ---- with index k
# C ------------ with index n

def merge(A: list, B: list):  # for already sorted lists
    C = [0] * (len(A)+len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):  # comparing elements from A and B step-by-step
        if A[i] <= B[k]:  # "=" needed for sorting to be stable (if elems are equal, we use elem from list A)
            C[n] = A[i]
            i += 1
        else:  # elif A[i] > B[k]:
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):  # pouring outstanding elements from A
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):  # pouring outstanding elements from B
        C[n] = B[k]
        k += 1
        n += 1
    return C


print(merge([1, 3, 5, 8, 9, 12], [2, 4, 6, 8, 10, 11]))


def merge_using_slicing(A: list, B: list):
    final_list = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            final_list.append(A[i])
            i += 1
        else:
            final_list.append(B[j])
            j += 1
    # while i < len(A):
    #     final_list.append(A[i:])
    # while j < len(B):
    #     final_list.append(B[j:])

    # if i < len(A):
    #     for k in range(i, len(A)):
    #         final_list.append(A[k])
    # elif j < len(B):
    #     for k in range(j, len(B)):
    #         final_list.append(B[k])
    final_list += A[i:] + B[j:]
    return final_list


def merge_sort(A):  # N * log2N complexity
    if len(A) <= 1:
        return
    middle = len(A) // 2
    left_part = [A[i] for i in range(middle)]  # creating sublists to conform to the interface of the function above
    right_part = [A[i] for i in range(middle, len(A))]
    merge_sort(left_part)
    merge_sort(right_part)
    C = merge(left_part, right_part)  # calling the function above
    for i in range(len(A)):
        A[i] = C[i]


def merge_sort_using_slicing(A):
    middle = len(A) // 2
    a1 = A[:middle]  # splitting the list into two parts of approx. same length
    a2 = A[middle:]

    if len(a1) > 1:  # if length of the first part > 1, we'll split it further
        a1 = merge_sort_using_slicing(a1)
    if len(a2) > 1:  # if length of the second part > 1, we'll split it further
        a2 = merge_sort_using_slicing(a2)

    return merge_using_slicing(a1, a2)  # merging 2 lists in 1 when their length is 1


a = [9, 5, -3, 4, 7, 8, -8]
a = merge_sort_using_slicing(a)
print(a)

# merge_sort
# [9, 5, -3]                         [4, 7, 8, -8]
# [9] [5, -3]                        [4, 7] [8, -8]
# [9] [5] [-3]                       [4] [7] [8] [-8]
#


def new_merge_sort(data: list, start: int, end: int):  # start and end are indices we're working with
    if start < end:
        mid = (start + end) // 2
        new_merge_sort(data, start, mid)
        new_merge_sort(data, mid + 1, end)
        new_merge(data, start, mid, end)


def new_merge(data: list, start: int, mid: int, end: int):
    # build temp array to avoid modifying the original contents
    temp = [0] * (end - start + 1)  # pre-allocated buffer of memory

    i = start
    j = mid + 1
    k = 0

    # While both sub-arrays have values, try and merge them in sorted order
    while i <= mid and j <= end:
        if data[i] <= data[j]:
            temp[k] = data[i]
            i += 1
        else:
            temp[k] = data[j]
            j += 1
        k += 1

    # Add the rest of the values from the left sub-array into the result after the right sub-array is exhausted
    while i <= mid:
        temp[k] = data[i]
        i += 1
        k += 1

    # Add the rest of the values from the right sub-array into the result after the left sub-array is exhausted
    while j <= end:
        temp[k] = data[j]
        j += 1
        k += 1

    i = start
    while i <= end:
        data[i] = temp[i - start]
        i += 1


data = [-5, 20, 10, 3, 2, 0]
new_merge_sort(data, 0, len(data) - 1)
print(data)


def merge(list_1: list[int], list_2: list[int]) -> list:  # helper function - merges two sorted lists
    merged_list = []

    while list_1 and list_2:
        if list_1[0] >= list_2[0]:
            merged_list.append(list_2[0])
            list_2 = list_2[1:]
        else:
            merged_list.append(list_1[0])
            list_1 = list_1[1:]

    if list_1:
        merged_list.extend(list_1)
    if list_2:
        merged_list.extend(list_2)

    return merged_list


print(merge([1, 3, 7, 8], [2, 4, 5, 6]))


def merge(list1, list2):
    combined = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    # if i == len(list1):
    #     combined.extend(list2)
    # if j == len(list2):
    #     combined.extend(list1)
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


print(merge([1, 2, 7, 8], [3, 4, 5, 6]))


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))  # 'merge' only takes in sorted lists which is why we need to further divide them into parts


print(merge_sort([3, 1, 4, 2]))
