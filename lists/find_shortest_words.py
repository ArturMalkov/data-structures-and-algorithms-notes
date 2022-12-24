def find_shortest_words(words: list[str]) -> str:
    shortest_word_length = len(words[0])

    for word in words:
        if len(word) < shortest_word_length:
            shortest_word_length = len(word)

    result = []
    for word in words:
        if len(word) == shortest_word_length:
            result.append(word)

    return " ".join(result)


print(find_shortest_words(["aaa", "aa", "b", "cc", "d", "eee"]))


# one iteration
def find_shortest_words(words: list[str]) -> str:
    shortest_word_length = len(words[0])
    result = []

    for word in words:
        if len(word) < shortest_word_length:
            shortest_word_length = len(word)
            result = [word]
        elif len(word) == shortest_word_length:
            result.append(word)

    return " ".join(result)


print(find_shortest_words(["aaa", "aa", "b", "cc", "d", "eee", "b"]))
