"""
242 leetcode problem

Anagrams - two words made up of exactly same set of characters
"""

# Time complexity: O(n) (to be precise - O(s+t), where 's' and 't' and lengths of words)
# Memory complexity: O(n) (to be precise - O(s+t) because of hashmaps used)

# to achieve O(1) memory complexity, it can be useful to sort both words and compare them.
# e.g.: return sorted(word1) == sorted(word2)


def is_anagram(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    count_word1 = {}
    count_word2 = {}

    for i in range(len(word1)):
        count_word1[word1[i]] = 1 + count_word1.get(word1[i], 0)
        count_word2[word2[i]] = 1 + count_word2.get(word2[i], 0)
        # if char not in count_word1:
        #     count_word1[char] = 1
        # else:
        #     count_word1[char] += 1

    for char in count_word1:
        if count_word1[char] != count_word2.get(char, 0):  # return Counter(word1) == Counter(word2)
            return False

    return True
