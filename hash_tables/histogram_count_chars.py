# my solution
def prepare_histogram_of_chars(word: str) -> None:
    chars_count = {}

    for char in word:
        if char not in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] += 1

    num_of_lines_to_print = 0
    for count in chars_count.values():
        if count > num_of_lines_to_print:
            num_of_lines_to_print = count

    for line in range(num_of_lines_to_print, -1, -1):
        res = ["#" for val in chars_count.values() if val - line > 0]
        print("".join(res))

    print("".join(sorted(chars_count, key=lambda x: chars_count[x], reverse=True)))


prepare_histogram_of_chars("Hello, world!")


# proposed solution
def print_chart(word):
    symbol_count = {}
    max_symbol_count = 0

    for char in word:
        if char not in symbol_count:
            symbol_count[char] = 0
        symbol_count[char] += 1
        max_symbol_count = max(max_symbol_count, symbol_count[char])

    sorted_unique_symbols = sorted(symbol_count)

    for row in range(max_symbol_count, 0, -1):
        for symbol in sorted_unique_symbols:
            if symbol_count[symbol] >= row:
                print("#", end="")
            else:
                print(" ", end="")
        print()

    print("".join(sorted_unique_symbols))


print_chart("Hello, world!")
