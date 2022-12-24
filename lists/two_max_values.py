def two_max_values(nums: list[int]) -> tuple:
    first_max_value, second_max_value = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
    # first_max_value = max(nums[0], nums[1])
    # second_max_value = min(nums[0], nums[1])

    for i in range(2, len(nums)):
        if nums[i] > first_max_value:
            second_max_value = first_max_value
            first_max_value = nums[i]
        elif nums[i] > second_max_value:
            second_max_value = nums[i]

    return first_max_value, second_max_value


print(two_max_values([1, 2]))
