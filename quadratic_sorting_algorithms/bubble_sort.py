def bubble_sort(A):  # battle inside each consecutive pair of numbers
    for bypass in range(1, len(A)):
        for k in range(0, len(A)-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A


print(bubble_sort([34, 456, 35, 5, 1, 155]))


def bubble_sort_better(some_list):
    for i in range(len(some_list)-1):  # N-1 iterations
        for j in range(len(some_list)-1-i):  # iterations through unsorted pairs
            if some_list[j] > some_list[j+1]:  # to inverse, we can change operator sign here
                some_list[j], some_list[j+1] = some_list[j+1], some_list[j]
    return some_list


print(bubble_sort_better([34, 456, 35, 5, 1, 155]))


def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


print(bubble_sort([4, 2, 6, 5, 1, 3]))
