# there's a sequence of n numbers and x.
# how many times is x encountered in that sequence?

def left_bin_search(left, right, check, check_params):
    while left < right:
        middle = (left + right) // 2
        if check(middle, check_params):
            right = middle
        else:
            left = middle + 1

    return left


def check_is_gte_x(index, params):
    seq, x = params
    return seq[index] >= x


def check_is_gt_x(index, params):
    seq, x = params
    return seq[index] > x


def find_first(seq, x, check):
    result = left_bin_search(0, len(my_list)-1, check, (seq, x))
    if not check(result, (seq, x)):
        return len(seq)

    return result


def count_x(seq, x):
    index_gt = find_first(seq, x, check_is_gt_x)
    index_ge = find_first(seq, x, check_is_gte_x)
    return index_gt - index_ge


target = 8
my_list = [1, 3, 3, 5, 6, 6, 8]

print(count_x(my_list, target))
