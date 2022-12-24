# brute force approach - O(n**3) time complexity
def count_zero_sum_ranges(nums: list[int]) -> 0:
    count_ranges = 0

    for i in range(len(nums)):  # left pointer
        for j in range(i+1, len(nums)+1):  # right pointer
            range_sum = 0
            for k in range(i, j):  # pointer running between left and right pointers
                range_sum += nums[k]
            if range_sum == 0:
                count_ranges += 1

    return count_ranges


print(count_zero_sum_ranges([0, 1, 0, 0, 1, 0, 0, 0, 1, 0]))


# brute force approach #2 - O(n**2) time complexity
def count_zero_sum_ranges(nums: list[int]) -> int:
    count_ranges = 0

    for i in range(len(nums)):  # left pointer
        range_sum = 0
        for j in range(i, len(nums)):  # right pointer
            range_sum += nums[j]
            if range_sum == 0:
                count_ranges += 1

    return count_ranges


print(count_zero_sum_ranges([0, 1, 0, 0, 1, 0, 0, 0, 1, 0]))


# optimized solution - O(n) time complexity
def count_prefix_nums(nums: list[int]) -> dict[int, int]:
    prefix_sum_by_value = {0: 1}
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum not in prefix_sum_by_value:
            prefix_sum_by_value[current_sum] = 0
        prefix_sum_by_value[current_sum] += 1

    return prefix_sum_by_value


def count_zero_sum_ranges(prefix_sum_by_value: dict[int, int]) -> int:
    count_ranges = 0

    for current_sum in prefix_sum_by_value:
        count_sum = prefix_sum_by_value[current_sum]
        count_ranges += count_sum * (count_sum - 1) // 2

    return count_ranges
