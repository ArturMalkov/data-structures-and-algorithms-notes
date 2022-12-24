def max_count_chars(word: str) -> int:
    count_dict = {}
    max_count = 0
    answer = None

    for char in word:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1

    for key in count_dict:
        if count_dict[key] > max_count:
            max_count = count_dict[key]
            answer = key

    return answer
