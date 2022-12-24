# find a minimum number of parents to add for them to be 1/3 of the school's supervisory board
# use binary search

def left_binary_search(left, right, check, check_params):
    while left < right:  # left is the left boundary (initially equals to 0 - if parents are already 1/3 of the board and no parents need to be added)
        middle = (left + right) // 2  # right is the right boundary (initially equals to n - current number of supervisory board members - if n parents will be added, they will always be more than 1/3 of the board)
        if check(middle, check_params):
            right = middle
        else:
            left = middle + 1

    return left


def count_parents(m, params):  # m is the number of parents to be added
    n, k = params  # n is the current number of supervisory board members, k - current number of parents
    return (k + m) * 3 >= n + m


board_count = 100
parents_count = 15
min_num_of_parents_needed = left_binary_search(0, board_count, count_parents, (board_count, parents_count))
print(min_num_of_parents_needed)
