"""
167 leetcode problem
"""

# Brute force - check all combinations of numbers - Time complexity: O(n**2) - n times for each number in the array

# Two pointer - optimally - we only traverse through the input once - Time complexity: O(n)

numbers_list = [1, 3, 4, 5, 7, 10, 11]
target = 9
# 1 + 11 = 12 > 9 - shift right pointer to the left
# 1 + 10 = 11 > 9 - shift right pointer to the left
# 1 + 7 = 8 < 9 - shift left pointer to the right
# 3 + 7 = 10 > 9 - shift right pointer to the left
# etc.


def two_sum(numbers: list, target: int) -> list[int]:
    left_pointer = 0  # starts at the beginning of the numbers list
    right_pointer = len(list) - 1  # starts at the end of the numbers list

    while left_pointer < right_pointer:  # we're guaranteed to get a solution no matter what
        current_sum = numbers[left_pointer] + numbers[right_pointer]

        if current_sum == target:
            return [left_pointer + 1, right_pointer + 1]
        elif current_sum > target:
            right_pointer -= 1
        else:
            left_pointer += 1
