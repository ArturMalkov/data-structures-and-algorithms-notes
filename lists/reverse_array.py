def reverse_array(A: list, N: int):  # A is an array (list), N is its length
    # for i in range(N):
    #     A[i] = A[N-1-i]  # IT DOESN'T WORK!
    # return A

    for i in range(N//2):
        A[i], A[N-1-i] = A[N-1-i], A[i]
    return A

    # OR
    # for i in range(N//2):
    #     tmp = A[N-1-i]
    #     A[N-1-i] = A[i]
    #     A[i] = tmp
    # return A


print(reverse_array([15, 99, 100, 5], 4))

# N//2 above is important!
# 5 99 100 15
# 5 100 99 15  # need to stop here! to avoid further overriding to initial state
# 5 99 100 15
# 15 99 100 5


# another solution
def reverse_array(num_list: list[int]) -> None:
    left_pointer = 0
    right_pointer = len(num_list) - 1

    while right_pointer > left_pointer:
        temp = num_list[left_pointer]
        num_list[left_pointer] = num_list[right_pointer]
        num_list[right_pointer] = temp
        left_pointer += 1
        right_pointer -= 1
