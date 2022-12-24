"""
1 leetcode problem
"""


# Brute force - check all combinations of numbers to see whether they add up to a target - Time complexity: O(n**2)

# One pass solution - O(n)
numbers = [2, 1, 5, 3]
target = 4

# for each number in a list we're looking for a difference between it and a target:
# 2 - looking for 2 to add up to 4
# 1 - looking for 3 to add up to 4 - we don't have to look for every number - we just need to know if 3 exists
# 5 - looking for -1 to add up to 4
# etc.

# the most efficient way - to make a hash map of every value in the numbers list so that we can instantly check if a
# particular value exists

# Time: O(n) - iterating through the list once + adding each value to a hash map which is O(1) operation + checking if
# it exists in hash map which is also O(1) operation
# Memory: O(n) - we're adding each value to a hash map


def two_sum(numbers: list[int], target: int) -> list[int]:
    prev_map = {}  # every element that comes before the current one

    for idx, num in enumerate(numbers):
        difference = target - num
        if difference in prev_map:
            return [prev_map[difference], idx]
        else:
            prev_map[num] = idx  # val : its index in the list


print(two_sum(numbers, target))
