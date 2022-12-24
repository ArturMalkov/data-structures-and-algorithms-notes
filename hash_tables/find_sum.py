# not optimal solution - O(n**2)
def two_terms_with_sum_x(nums: list[int], target_sum: int) -> tuple[int, int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                return nums[i], nums[j]
    return 0, 0


print(two_terms_with_sum_x([4, 2, 3, 5], 8))


# optimized solution - O(n)
def two_terms_with_sum_x(nums: list[int], target_sum: int) -> tuple[int, int]:
    prev_nums = set()  # store all processed numbers in a set

    for current_num in nums:
        if target_sum - current_num in prev_nums:
            return current_num, target_sum - current_num
        prev_nums.add(current_num)

    return 0, 0


print(two_terms_with_sum_x([1, 3, 5, 8, 2], 7))
