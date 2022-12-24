def check_sorted(A, ascending=True):
    """Checks whether the list is sorted for O(N) (O(len(A)))"""
    flag = True
    s = 2 * int(ascending) - 1  # int(True) = 1, int(False) = 0
    for i in range(len(A)-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break

    return flag
