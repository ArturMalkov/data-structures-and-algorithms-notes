def recursive_summation(num):
    if num <= 1:
        return num
    return num + recursive_summation(num-1)


print(recursive_summation(10))
