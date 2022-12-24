# O(NK**2 + M) solution
# M is the number of words in the text
# N is the length of a dictionary
# K is the max number of characters in a word
# O(NK) - throwing one character from a word in all possible ways
def is_word_in_dict(dictionary: list[str], text: list[str]) -> list[bool]:
    good_words = set(dictionary)

    for word in dictionary:
        for del_position in range(len(word)):
            good_words.add(word[:del_position] + word[del_position+1:])

    answer = []
    for word in text:
        answer.append(word in good_words)

    return answer

