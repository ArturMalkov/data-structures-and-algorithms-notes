def array_circular_shift_left(A, N):  # A is an array (list), N is its length
    tmp = A[0]
    for i in range(N-1):
        A[i] = A[i+1]
    A[N-1] = tmp
    return A


print(array_circular_shift_left([1, 2, 3, 4, 0], 5))  # 2, 3, 4, 0, 1


def array_circular_shift_right(A, N):
    tmp = A[N-1]
    for i in range(N-1, 0, -1):
        A[i] = A[i-1]
    A[0] = tmp
    return A

    # OR

    # tmp = A[N-1]
    # for i in range(N-2, -1, -1):
    #     A[i+1] = A[i]
    # A[0] = tmp
    # return A


print(array_circular_shift_right([1, 2, 3, 4, 0], 5))  # 0, 1, 2, 3, 4
