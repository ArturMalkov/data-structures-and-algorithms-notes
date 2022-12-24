def make_prefix_zeros(nums: list[int]) -> list[int]:
    prefixed_zeros = [0] * (len(nums) + 1)

    for i in range(1, len(nums) + 1):
        if nums[i-1] == 0:
            prefixed_zeros[i] = prefixed_zeros[i-1] + 1
        else:
            prefixed_zeros[i] = prefixed_zeros[i-1]

    return prefixed_zeros


# O(1) time complexity
def count_zeros(prefix_zeros: list[int], left: int, right: int) -> int:
    return prefix_zeros[right] - prefix_zeros[left]


# "2021-07-15/1" от 15.07.2021
