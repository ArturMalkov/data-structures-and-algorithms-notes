def max_num_search(list1):
    max_num = list1[0]
    for i in range(len(list1)):
        if max_num < list1[i]:
            max_num = list1[i]
    return max_num

    # OR
    # max_num = list1[0]
    # for elem in list1:
    #     if max_num < elem:
    #         max_num = elem
    # return max_num


print(max_num_search([5, 3, 1, 100, 9, 1000, 654]))


def min_num_search(list1):
    min_num = list1[0]
    for i in range(len(list1)):
        if min_num > list1[i]:
            min_num = list1[i]
    return min_num


print(min_num_search([5, 4, 15, 67, 2, 9, 0, 2, 3]))
