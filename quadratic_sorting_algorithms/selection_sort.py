def selection_sort(A):
    for pos in range(len(A)-1):  # once the battle for a particular place is ended, we move to the next place's battle
        for k in range(pos+1, len(A)):  # shift the beginning of the area being sorted (do not touch already sorted prev pos)
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


print(selection_sort([4, 2, 5, 1, 3]))
# 2 4 5 1 3


def selection_sort_reversed(my_list):
    for pos in range(len(my_list)-1):
        for val in range(pos+1, len(my_list)):
            if my_list[pos] < my_list[val]:
                my_list[pos], my_list[val] = my_list[val], my_list[pos]
    return my_list


print(selection_sort_reversed([4, 2, 5, 1, 3]))


def selection_sort(my_list):  # 4 2 6 5 1 3
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j

        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list


print(selection_sort([4, 2, 6, 5, 1, 3]))
