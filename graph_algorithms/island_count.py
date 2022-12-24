"""
Time complexity: O(rc) - where 'r' is the number of rows, 'c' is the number of columns.
Space complexity: O(rc) - adding visited positions to a set.
"""

# "W" stands for water, "L" stands for land
grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]


# ??????????????????????????????????
def island_count(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if explore(grid, row, column, visited):
                count += 1
    return count


def explore(grid, row, column, visited):
    row_in_bounds = 0 <= row < len(grid)
    column_in_bounds = 0 <= column < len(row)
    if not row_in_bounds or not column_in_bounds:  # we shouldn't consider invalid position
        return False

    if grid[row][column] == "W":
        return False

    position = f"{row},{column}"
    if position in visited:
        return False  # indicates that this is not a new island we're exploring
    visited.add(position)

    explore(grid, row-1, column, visited)  # depth-first traversal - neighbors up, down, left and right
    explore(grid, row+1, column, visited)
    explore(grid, row, column-1, visited)
    explore(grid, row, column+1, visited)

    return True


print(island_count(grid))
