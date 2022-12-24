import math


def decode_chiffre(numbers_count, values):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' ']

    result = []

    for i in range(len(values)):
        if i == 0:
            char_index = int(math.log2(values[i]))
        else:
            char_index = int(math.log2(values[i] - values[i-1]))

        result.append(alphabet[char_index])

    return "".join(result)
# # #
# # #
print(decode_chiffre(5, [1, 2049, 2305, 2309, 2325]))
print(decode_chiffre(12, [4, 132, 148, 262292, 262420, 393492, 67502336, 67502337, 68026625
]))

