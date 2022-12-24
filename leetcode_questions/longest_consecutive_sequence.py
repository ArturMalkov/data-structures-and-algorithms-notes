"""
128 leetcode problem
"""

# Brute force approach - sorting solution
# Time complexity: O(log n) - because sorting is O(log n)


# Optimal solution
# Time: O(n)
# Memory: O(n) - we're creating a set

nums = [100, 4, 200, 1, 3, 2]


def longest_consecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    longest = 0

    for n in nums:
        # check if it's the start of the sequence
        if n - 1 not in nums_set:
            length = 0
            while (n + length) in nums:
                length += 1
            if length > longest:
                longest = length
    return longest
