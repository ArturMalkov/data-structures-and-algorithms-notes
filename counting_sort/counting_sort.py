def counting_sort(nums: list[int]) -> list[int]:
    min_value = min(nums)
    max_value = max(nums)
    k = (max_value - min_value) + 1  # number of possible values
    count = [0] * k

    for num in nums:
        count[num - min_value] += 1

    current_pos = 0
    for val in range(0, k):
        for i in range(count[val]):
            nums[current_pos] = val + min_value
            current_pos += 1

    return nums
