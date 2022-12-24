"""
Time complexity: O(rc) - where "r" is the number of rows, "c" is the number of columns.
Space complexity: O(rc)
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


#??????????????
def minimum_island(grid):
    visited = set()

    min_size = 1_000_000_000  # better use positive infinity
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            size = explore_size(grid, row, column, visited)
            if 0 < size < min_size:
                min_size = size
    return min_size


def explore_size(grid, row, column, visited):
    row_in_bounds = 0 <= row < len(grid)
    column_in_bounds = 0 <= column <= len(grid[0])
    if not row_in_bounds or not column_in_bounds:
        return 0  # to be consistent with return types

    if grid[row][column] == "W":
        return 0

    position = f"{row},{column}"  # use str since we cannot add a list to the set (it is not hashable)
    if position in visited:
        return 0
    visited.add(position)

    size = 1
    size += explore_size(grid, row-1, column, visited)
    size += explore_size(grid, row+1, column, visited)
    size += explore_size(grid, row, column-1, visited)
    size += explore_size(grid, row, column+1, visited)
    return size


print(minimum_island(grid))
