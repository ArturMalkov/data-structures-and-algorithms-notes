"""
42 leetcode problem
"""


# O(n) memory complexity solution
def calculate_water(elevation_map: list[int]) -> int:  # 0 1 0 2 1 0 1 3 2 1 2 1
    max_left = [0]
    max_right = []

    for i in range(1, len(elevation_map)):
        max_left.append(max(elevation_map[:i]))

    for i in range(len(elevation_map)-1, -1, -1):
        max_right.insert(0, (max(elevation_map[i:])))

    rain_amount = 0
    for left, right, elevation in zip(max_left, max_right, elevation_map):
        if min(left, right) > elevation:
            rain_amount += min(left, right) - elevation

    return rain_amount


print(calculate_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# O(1) memory complexity solution
def trap(height: list[int]) -> int:
    # edge case check
    if not height:
        return 0

    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    result = 0

    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            result += left_max - height[l] if left_max - height[l] > 0 else 0
        else:
            r -= 1
            right_max = max(right_max, height[r])
            result += right_max - height[r] if right_max - height[r] > 0 else 0

    return result


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
