def sort2(first, second):
    if first < second:
        return first, second
    return second, first


def is_able_to_break_free(a, b, c, d, e):
    # to put the max value out of variables a, b and c into variable c
    a, b, = sort2(a, b)
    b, c = sort2(b, c)

    # to put the max value (after c) into variable b
    a, b, = sort2(a, b)

    # to put values into variables d and e in increasing order
    d, e = sort2(d, e)

    return a <= d and b <= e


# 4276 0140 3621 9244
# 06/22
# 370
