def find_kth_largest_element(array: list[int], k: int) -> int:
    i = k

    while i != 0:
        max_value = array[0]
        for j in range(len(array[1:])):
            if array[j] > max_value:
                max_value = array[j]
        array.remove(max_value)
        i -= 1

    return max_value


print(find_kth_largest_element([4, 2, 9, 7, 5, 6, 7, 1, 3], 4))
print(find_kth_largest_element([4, 2, 9, 7, 5, 6, 7, 1, 3], 5))


# simpler form:
def find_kth_largest_element(array: list[int], k: int) -> int:
    for i in range(k-1):
        array.remove(max(array))
    return max(array)
