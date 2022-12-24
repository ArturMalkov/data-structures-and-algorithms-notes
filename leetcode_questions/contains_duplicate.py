"""
217 leetcode problem
"""


# brute force approach - comparing each value with all other elements in the array:
# Time Complexity - O(n**2) where n is the size of the array
# Space Complexity - O(1) - no extra space required


# better solution - working on a sorted array - checking adjacent numbers
# Time Complexity - O(log n) - because of sorting
# Space Complexity - O(1)


# one more solution - working with a hash set - checking if a particular number is already there
# Time Complexity - O(1)
# Space Complexity - O(n) - space used to create a set (tradeoff) - up to the size of the input array


array = [1, 2, 3, 4]


def contains_duplicate(nums: list[int]) -> bool:
    hash_set = set()

    for elem in nums:
        if elem in hash_set:
            return True
        else:
            hash_set.add(elem)
    return False
