def make_prefix_sum(nums: list[int]) -> list[int]:
    prefix_sum = [0] * (len(nums) + 1)

    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

    return prefix_sum


# O(1) time complexity
def range_sum_query(prefix_sum: list[int], left: int, right: int) -> int:
    return prefix_sum[right] - prefix_sum[left]
