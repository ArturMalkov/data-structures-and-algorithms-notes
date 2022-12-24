def trapping_rain_water(heights: list[int]) -> int:
    max_pos = 0
    for i in range(len(heights)):
        if heights[i] > heights[max_pos]:
            max_pos = i

    result = 0

    current_max_height = 0
    for i in range(max_pos):
        if current_max_height < heights[i]:
            current_max_height = heights[i]
        else:
            result += current_max_height - heights[i]

    current_max_height = 0
    for i in range(len(heights)-1, max_pos, -1):
        if current_max_height < heights[i]:
            current_max_height = heights[i]
        else:
            result += current_max_height - heights[i]

    return result


print(trapping_rain_water([3, 1, 4, 3, 5, 1, 1, 3, 1]))
