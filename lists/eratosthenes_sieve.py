def eratosthenes_sieve(N):
    A = [True] * N
    A[0] = A[1] = False

    for i in range(2, N):
        if A[i]:
            for j in range(2*i, N, i):
                A[j] = False

# F F T T T T T T T T T
# F F T T F T F T F T F
