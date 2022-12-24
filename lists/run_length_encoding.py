# my solution
def rle(word: str) -> str:
    result = ""
    count = 1

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            count += 1
        else:
            final_count = str(count) if count != 1 else ""
            result += word[i] + final_count
            count = 1

    final_count = str(len(word[i+1:])) if len(word[i+1:]) != 1 else ""
    result += word[i+1] + final_count

    return result


print(rle("AAABBVIE"))


def get_unique_chars(word):
    last_char = word[0]
    result = []

    for i in range(1, len(word)):
        if word[i] != last_char:
            result.append(last_char)
            last_char = word[i]

    result.append(last_char)
    return result


print(get_unique_chars("aaabbvie"))


# suggested solution
def rle(word: str) -> str:
    def pack(char, count):
        if count > 1:
            return char + str(count)
        return char

    last_char = word[0]
    result = []
    count = 1

    for i in range(1, len(word)):
        if last_char != word[i]:
            result.append(pack(last_char, count))
            count = 1
        else:
            count += 1
        last_char = word[i]

    result.append(pack(last_char, count))

    return "".join(result)


print(rle("abbviee"))


# another approach
def rle(word: str) -> str:
    def pack(char, count):
        if count > 1:
            return char + str(count)
        return char

    last_char = word[0]
    last_pos = 0
    result = []

    for i in range(1, len(word)):
        if word[i] != last_char:
            result.append(pack(last_char, i - last_pos))
            last_pos = i
        last_char = word[i]

    result.append(pack(last_char, len(word) - last_pos))

    return "".join(result)


print(rle("aaabbviee"))
