def greatest_common_divisor(num1, num2):
    min_value = min(num1, num2)
    gcd = 0

    for num in range(1, min_value):
        if num1 % num == 0 and num2 % num == 0:
            if num > gcd:
                gcd = num

    return gcd


print(greatest_common_divisor(15, 20))
