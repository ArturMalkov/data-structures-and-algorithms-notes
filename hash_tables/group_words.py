def group_words(words: list[str]) -> list:
    groups = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)

    result = []
    for sorted_word in groups:
        result.append(groups[sorted_word])

    return result
