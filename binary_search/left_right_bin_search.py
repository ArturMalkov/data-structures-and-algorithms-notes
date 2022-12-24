# left is the minimum possible value, right is the maximum possible value
def left_bin_search(left, right, check_func, check_params):
    """returns first appropriate value which matches our requirements"""
    while left < right:
        middle = (left + right) // 2
        if check_func(middle, check_params):  # checks if everything is OK - if it already is, we need to search for the first (!) appropriate value on the left
            right = middle
        else:
            left = middle + 1

    return left


def right_bin_search(left, right, check_func, check_params):
    """returns last appropriate value which matches our requirements"""
    while left < right:
        middle = (left + right + 1) // 2
        if check_func(middle, check_params):  # checks if everything is OK - if it already is, we need to search for the last (!) appropriate value on the right
            left = middle
        else:
            right = middle - 1

    return left
