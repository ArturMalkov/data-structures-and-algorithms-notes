# there is a blackboard of width w and height h. We need to place n square stickers on that blackboard.
# what's the maximum length of a sticker's side such that all n stickers can be placed on the blackboard?
def right_binary_search(left, right, check, check_params):
    while left != right:
        middle = (left + right + 1) // 2
        if check(middle, check_params):
            left = middle
        else:
            right = middle - 1

    return left


def check_stickers(size, params):
    n, w, h = params  # n is the number of stickers, w and h are blackboard measurements
    return (w // size) * (h // size) >= n
