def rectangles_intersections(rectangles: list[list[tuple, tuple]]):
    result = []

    for i in range(len(rectangles)):
        intersections = 0
        for j in range(i, len(rectangles)):
            if rectangles[i][0] < rectangles[j][0] or rectangles[i][1] > rectangles[j][1]:
                intersections += 1
        result.append(intersections)

    return result


rectangles = [
    [(-2, -4), (2, 2)],
    [(-2, -4), (0, -1)],
    [(-2, -1), (0, 2)],
    [(0, -4), (2, -1)],
    [(0, -1), (2, 2)],
    [(-1, -2), (1, 0)],
]


print(rectangles_intersections(rectangles))

