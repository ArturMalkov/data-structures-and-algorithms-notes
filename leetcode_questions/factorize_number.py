def factorize_number(x):
    if x == 0:
        return

    factors = []
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            factors.append(divisor)
            x /= divisor
        else:
            divisor += 1

    return factors


print(factorize_number(1024))
print(factorize_number(999))
