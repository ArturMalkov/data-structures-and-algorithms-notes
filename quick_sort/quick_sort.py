"""
QuickSort or Tony Hoare sort
O(n*logN) - for unsorted data (and O(n**2) for already sorted data)
To avoid O(n2) time complexity, it's recommended to randomly choose middle element on each iteration
(instead of simply choosing the first element)
"""


def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    left_part = []
    middle_part = []
    right_part = []
    for x in A:
        if x < barrier:
            left_part.append(x)
        elif x == barrier:
            middle_part.append(x)
        else:
            right_part.append(x)
    hoar_sort(left_part)
    hoar_sort(right_part)
    k = 0
    for x in left_part + middle_part + right_part:
        A[k] = x
        k += 1


def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_recursive(left) + middle + quicksort_recursive(right)


### another approach
def swap(my_list, index1, index2):  # helper function
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):  # helper function
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            # my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
            swap(my_list, swap_index, i)
    # my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]
    swap(my_list, pivot_index, swap_index)
    return swap_index


my_list = [4, 6, 1, 7, 3, 2, 5]
print(pivot(my_list, 0, 6))
print(my_list)


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))

