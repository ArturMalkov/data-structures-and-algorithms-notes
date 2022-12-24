from copy import deepcopy


figure = [
    ["............."],
    ["...._........"],
    [".._/A\_..._.."],
    ["./B\_/D\_/F\."],
    [".\_/C\_/E\_/."],
    ["...\_/G\_/..."],
    [".....\_/....."],
    ["............."]
]


def reverse_figure(columns, rows, figure):
    # new_figure = ("." * columns + "\n") * rows
    new_figure = deepcopy(figure)

    for i in range(rows):
        for j in range(columns):
            if figure[i][j] == ".":
                continue
            elif figure[i][j] == "/":
                new_figure[rows-1-i][columns-1-j] = "\\"
            elif figure[i][j] == "\\":
                new_figure[rows-1-i][columns-1-j] = "/"
            elif figure[i][j] == "_":
                new_figure[rows-1-i][columns-1-j] = "_"
            else:
                pass

    return new_figure


print(reverse_figure(13, 8, figure))

