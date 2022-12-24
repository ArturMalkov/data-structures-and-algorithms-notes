# get the longest sequence of increasing unique numbers
def longest_sequence(nums):
    max_length = 1
    current_length = 1

    left, right = 0, 1

    while right < len(nums):
        if nums[right] == nums[left] + 1:
            current_length += 1
            left += 1
        else:
            current_length = 1
            left = right
        max_length = max(max_length, current_length)
        right += 1

    return max_length


print(longest_sequence([1]))
print(longest_sequence([1, 1, 1, 1, 1]))
print(longest_sequence([1, 2, 3, 3, 2, 1]))
print(longest_sequence([1, 2, 3, 4, 5]))
print(longest_sequence([1, 2, 3, 3, 4, 5, 6]))
print(longest_sequence([1, 2, 3, 4, 5, 2, 2]))
print(longest_sequence([1, 2, 3, 2, 2, 6, 7, 1]))
