def insert_element_at_the_beginning(my_list, list_length, element):
    tmp = my_list[list_length-1]
    for i in range(list_length-1, 0, -1):
        my_list[i] = my_list[i-1]
    my_list[list_length-1] = tmp
    my_list[0] = element
    return my_list


print(insert_element_at_the_beginning([15, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 100))
# 0 1 2 3 4 5 6 7 8