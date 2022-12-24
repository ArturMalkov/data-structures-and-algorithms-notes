"""
Function takes in a target sum and an array of numbers.
Function should return a boolean indicating whether or not it's possible to generate the target sum using numbers from
the array.
"""


# Brute force approach
# Time complexity: O(n^m), where m is a target sum and n is the array length
# Space complexity: O(m)
def can_sum(target_sum: int, numbers: list) -> bool:
    # base case 1
    if target_sum == 0:
        return True
    # base case 2
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers):  # we can reuse the same number as many times as we want
            return True
    return False


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
# print(can_sum(300, [7, 14]))


# Time complexity: O(mn)
# Space complexity: O(m)
def can_sum_memoized(target_sum: int, numbers: list, memo=None) -> bool:
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum_memoized(remainder, numbers, memo):
            memo[remainder] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum_memoized(7, [2, 3]))
print(can_sum_memoized(7, [5, 3, 4, 7]))
print(can_sum_memoized(7, [2, 4]))
print(can_sum_memoized(8, [2, 3, 5]))
print(can_sum_memoized(300, [7, 14]))
