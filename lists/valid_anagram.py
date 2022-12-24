def are_valid_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)  # O(nlogn) time complexity


# another approach - Time complexity: O(n); Space complexity: O(n)
def are_valid_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for char in s1:
        if char in freq1:  # O(1) operation made n times
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in s2:
        if char in freq2:  # O(1) operation made n times
            freq2[char] += 1
        else:
            freq2[char] = 1

    # return freq1 == freq2
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:  # O(1) operation made n times
            return False
    return True


# Counter from 'collections' module can be used instead
from collections import Counter


def are_valid_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)
