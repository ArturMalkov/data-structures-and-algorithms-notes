def array_search(A: list, N: int, x: int):  # A - array (list), N - its length, x - search value
    for i in range(N):
        if A[i] == x:
            return i
    return None
