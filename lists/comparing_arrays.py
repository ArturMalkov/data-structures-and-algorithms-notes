def compare_arrays(list1, list2, length):  # length is a length of each array (the same for both arrays)
    """Returns the biggest array."""
    for i in range(length):
        if list1[i] > list2[i]:
            return list1
        elif list1[i] < list2[i]:
            return list2
    return "Lists are equal"


print(compare_arrays([1, 29, 3], [5, 67, 95], 3))
