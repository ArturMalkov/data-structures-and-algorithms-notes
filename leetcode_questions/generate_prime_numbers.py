# generate prime numbers in range n
def generate_primes(n: int) -> list[int]:
    result = []

    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)

    return result


print(generate_primes(10))

