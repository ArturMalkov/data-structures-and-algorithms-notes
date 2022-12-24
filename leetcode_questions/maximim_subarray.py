"""
53 leetcode problem
"""

input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# Brute force approach - O(n^3) or O(n^2)
# 3 or 2 nested for loops

# Optimal solution - O(n)
def max_subarray(nums: list[int]) -> int:
    max_subarr = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_subarr = max(max_subarr, current_sum)

    return max_subarr


print(max_subarray(input_array))
