# we are given a sorted sequence of n numbers and x.
# what is the index of the first number in the sequence which is >= x? if no such number exists, return n
def left_binary_search(left, right, check, check_params):
    while left < right:
        middle = (left + right) // 2
        if check(middle, check_params):
            right = middle
        else:
            left = middle + 1

    return left


def check_is_gte(index, params):
    seq, x = params
    return seq[index] >= x


def find_first_gte(seq, x):
    result = left_binary_search(0, len(seq)-1, check_is_gte, (seq, x))
    if seq[result] < x:
        return len(seq)

    return result


my_list = [1, 3, 3, 5, 6, 6, 8]
print(find_first_gte(my_list, 7))
