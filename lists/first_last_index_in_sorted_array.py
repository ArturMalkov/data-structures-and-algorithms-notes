# Time complexity: O(n); Space complexity: O(1)
def first_and_last_index(array: list[int], target: int) -> list[int]:
    for i in range(len(array)):
        if array[i] == target:
            start = i
            while i + 1 < len(array) and array[i+1] == target:
                i += 1
            finish = i
            return [start, finish]

    return [-1, -1]


arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5
print(first_and_last_index(arr, target))


# since an array is sorted, we can use a binary search
def find_start(array: list[int], target: int) -> int:
    if array[0] == target:
        return 0

    left, right = 0, len(array) - 1

    while left < right:
        mid = len(array) // 2
        if array[mid] == target and array[mid-1] < target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def first_and_last_index(array: list[int], target: int) -> list[int]:
    if len(array) == 0:
        return [-1, -1]

    start = find_start(array, target)
    if start == -1:
        return [-1, -1]
    end = start
    while end + 1 < len(array) and array[end + 1] == target:
        end += 1

    return [start, end]


def find_end(array: list[int], target: int) -> int:
    if array[-1] == target:
        return len(array) - 1

    left, right = 0, len(array) - 1

    while left < right:
        mid = (left + right) // 2
        if array[mid] == target and array[mid+1] > target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def first_and_last_index(array: list[int], target: int) -> list[int]:
    if len(array) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]

    start = find_start(array, target)
    end = find_end(array, target)

    return [start, end]
