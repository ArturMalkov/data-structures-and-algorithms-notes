"""
Function takes in a target_sum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up to exactly the target_sum.
In case multiple combinations are possible, you may return any single one.
"""


def how_sum(target_sum: int, numbers: list) -> list:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if remainder_result is not None:
            return [*remainder_result, num]

    return None


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
