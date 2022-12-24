def is_symmetric_sequence(sequence: list[int]) -> bool:
    if len(sequence) % 2 == 0:
        r = len(sequence) // 2
        l = r - 1
    else:
        mid = len(sequence) // 2
        l = mid - 1
        r = mid + 1

    while l >= 0:
        if sequence[l] == sequence[r]:
            l -= 1
            r += 1
        else:
            return False

    return True


print(is_symmetric_sequence([1, 2, 3, 4, 5, 4, 3, 2, 1]))
print(is_symmetric_sequence([1, 2, 3, 0, 3, 2, 1]))
print(is_symmetric_sequence([1, 2, 3, 0, 4, 3, 2, 1]))


# O(n**2) solution
def fill_symmetric_sequence(sequence: list[int]) -> list[int]:
    for start in range(len(sequence)):
        i = start
        j = len(sequence) - 1
        while i < len(sequence) and i <= j and sequence[i] == sequence[j]:
            i += 1
            j -= 1
        if i > j:
            result = []
            for k in range(start, -1, -1):
                result.append(sequence[k])

            return result


print(fill_symmetric_sequence([1, 2, 3, 4, 5, 4, 3, 2, 1]))
print(fill_symmetric_sequence([1, 2, 3, 0, 3, 2, 1]))
print(fill_symmetric_sequence([1, 2, 3, 0, 4, 3, 2, 1]))
