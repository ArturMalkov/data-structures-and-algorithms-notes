def count_beating_rooks(rook_coords: tuple[int, int]) -> int:
    def add_rook(row_or_col, key):
        if key not in row_or_col:
            row_or_col[key] = 0
        row_or_col[key] += 1

    def count_pairs(row_or_col):
        pairs = 0
        for key in row_or_col:
            pairs += row_or_col[key] - 1
        return pairs

    rooks_in_row = {}
    rooks_in_col = {}

    for row, col in rook_coords:
        add_rook(rooks_in_row, row)
        add_rook(rooks_in_col, col)

    return count_pairs(rooks_in_row) + count_pairs(rooks_in_col)

