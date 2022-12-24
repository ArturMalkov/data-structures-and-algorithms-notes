def compare_two(value_1, value_2):
    if value_1 > value_2:
        return value_1, value_2
    return value_2, value_1


def largest_product_three_nums(nums: list[int]) -> int:
    max_1, max_2 = compare_two(nums[0], nums[1])
    max_2, max_3 = compare_two(max_2, nums[2])
    max_1, max_2 = compare_two(max_1, max_2)

    for i in range(3, len(nums)):
        if nums[i] > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = nums[i]
        elif nums[i] > max_2:
            max_3 = max_2
            max_2 = nums[i]
        elif nums[i] > max_3:
            max_3 = nums[i]

    # what should we do with negative numbers???

    return max_1 * max_2 * max_3


print(largest_product_three_nums([1, 2, 3, 4, 5, 6]))
print(largest_product_three_nums([1, 7, 0, 11, 5, 2]))
print(largest_product_three_nums([1, 2, 3, -4, 5, 6]))
print(largest_product_three_nums([1, -7, 0, -11, 5, 2]))


# proposed solution
def kth_rearrange(sequence, k):
    left = 0
    right = len(sequence) - 1

    while left < right:
        x = sequence[(left + right) // 2]
        equal_x_first = left
        greater_than_x_first = left

        for i in range(left, right + 1):
            now = sequence[i]
            if now == x:
                sequence[i] = sequence[greater_than_x_first]
                sequence[greater_than_x_first] = now
                greater_than_x_first += 1
            elif now < x:
                sequence[i] = sequence[greater_than_x_first]
                sequence[greater_than_x_first] = sequence[equal_x_first]
                sequence[equal_x_first] = now
                greater_than_x_first += 1
                equal_x_first += 1

        if k < equal_x_first:
            right = equal_x_first - 1
        elif k > greater_than_x_first:
            left = greater_than_x_first
        else:
            return


kth_rearrange([1, 7, 0, 11, 5, 2], 3)
