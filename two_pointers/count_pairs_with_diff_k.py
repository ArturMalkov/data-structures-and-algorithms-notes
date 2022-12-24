# count pairs of numbers A, B in nums where A - B > K (nums is a sorted array)


# brute force approach - O(n**2) solution
def count_pairs_with_diff_gt_k(nums: list[int], k: int) -> int:
    pair_count = 0

    for first in range(len(nums)):
        for last in range(first+1, len(nums)):
            if nums[last] - nums[first] > k:
                pair_count += 1

    return pair_count


print(count_pairs_with_diff_gt_k([1, 3, 7, 8], 4))


# optimized solution - O(n) time complexity
def count_pairs_with_diff_gt_k(nums: list[int], k: int) -> int:
    pair_count = 0

    left_pointer = 0
    right_pointer = 1

    while right_pointer < len(nums):
        if nums[right_pointer] - nums[left_pointer] <= k:
            right_pointer += 1
        else:
            pair_count += len(nums[right_pointer:])
            left_pointer += 1

    return pair_count


print(count_pairs_with_diff_gt_k([1, 3, 7, 8], 4))


# proposed solution
def count_pairs_with_diff_gt_k(nums: list[int], k: int) -> int:
    count_pairs = 0
    last = 0

    for first in range(len(nums)):
        while last < len(nums) and nums[last] - nums[first] <= k:
            last += 1
        count_pairs += len(nums) - last

    return count_pairs


print(count_pairs_with_diff_gt_k([1, 3, 7, 8], 4))
