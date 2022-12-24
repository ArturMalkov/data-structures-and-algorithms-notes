"""
You are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner.
You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?
"""


# Brute force approach
# Time complexity: O(2^(n+m))
# Space complexity: O(n+m)
def grid_traveler(rows, columns):
    if rows == 1 and columns == 1:
        return 1
    if rows == 0 or columns == 0:  # grid is empty, so there's no way to travel through it
        return 0
    return grid_traveler(rows - 1, columns) + grid_traveler(rows, columns - 1)


# print(grid_traveler(1, 1))
# print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
# print(grid_traveler(3, 3))
# print(grid_traveler(18, 18))

# x x
# x x
# x x

#          2 2                             3 1
#   1 2            2 1             2 1             3 0
# 0 2  1 1     1 1    2 0       1 1   2 0


# Approach with memoization
# Time complexity: O(m*n)
# Space complexity: O(n+m)
def grid_traveler_memoized(rows, columns, memo=None):
    if memo is None:
        memo = {}
    key = f"{rows},{columns}"

    if key in memo:
        return memo[key]
    if rows == 1 and columns == 1:
        return 1
    if rows == 0 or columns == 0:
        return 0
    memo[key] = grid_traveler_memoized(rows-1, columns, memo) + grid_traveler_memoized(rows, columns-1, memo)
    return memo[key]


print(grid_traveler_memoized(1, 1))
print(grid_traveler_memoized(2, 3))
print(grid_traveler_memoized(3, 2))
print(grid_traveler_memoized(3, 3))
print(grid_traveler_memoized(18, 18))
