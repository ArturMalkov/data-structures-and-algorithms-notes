def find_min_even_number(nums):
    min_even_number = -1

    for i in range(len(nums)):
        if nums[i] % 2 == 0 and (min_even_number == -1 or nums[i] < min_even_number):
            min_even_number = nums[i]

    return min_even_number


print(find_min_even_number([-99, 25, 46, 20, -100, 22]))


def find_min_even_number(nums):
    found_even_number = False
    min_even_number = -1

    for i in range(len(nums)):
        if nums[i] % 2 == 0 and (not found_even_number or nums[i] < min_even_number):
            min_even_number = nums[i]
            found_even_number = True

    return min_even_number


print(find_min_even_number([-99, 25, 46, 20, -100, 22]))


def find_min_even_number(nums):
    even_numbers = [num for num in nums if num % 2 == 0]
    if not even_numbers:
        return -1

    min_even_number = even_numbers[0]

    for i in range(1, len(even_numbers)):
        if even_numbers[i] < min_even_number:
            min_even_number = even_numbers[i]

    return min_even_number


print(find_min_even_number([-99, 25, 46, 20, -100, 22]))