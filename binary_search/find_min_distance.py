# there is a bicycle race competition with n athletes.
# at the very beginning, each of them is away from start line by x1, x2, ..., xn meters.
# each athlete has his/her own permanent speed of v1, v2, ..., vn meters per second.
# at which point in time will the distance between the leader and the loser be minimal?
def f_bin_search(left, right, eps, check, params):
    while left + eps < right:
        middle = (left + right) / 2
        if check(middle, eps, params):
            right = middle
        else:
            left = middle

    return left


def check_ascending(time, eps, params):
    """Checks if the distance is increasing"""
    return dist(time + eps, params) >= dist(time, params)  # if it's True, the distance is increasing and we need to shift the right search bound


def dist(time, params):
    """Checks the distance between the leader and the loser at a particular time"""
    x, v = params
    min_pos = max_pos = x[0] + v[0] * time

    for i in range(1, len(x)):
        now_pos = x[i] + v[i] * time
        min_pos = min(min_pos, now_pos)
        max_pos = max(max_pos, now_pos)

    value = max_pos - min_pos
    return value