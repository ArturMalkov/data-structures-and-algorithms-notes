def is_simple_number(x):
    if x == 1:
        return False
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True
