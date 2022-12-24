# A shopping mall has N parking places (from 1 to N). There were M cars in total, some of them occupied several consecutive
# parking places. We know arrival and departure time for each car + the number of parking places it occupied.
# Were there moments in time when all parking places were occupied?
# If yes, define the minimum number of cars at these moments. If not, return M + 1
def min_cars_on_full_parking(n, cars):
    events = []

    for car in cars:
        arrival_time, departure_time, place_from, place_to = car
        events.append((arrival_time, 1, place_from - place_to + 1))
        events.append((departure_time, -1, place_from - place_to + 1))

    events.sort()
    occupied_places = 0
    current_cars = 0
    min_cars = len(cars) + 1

    for event in events:
        if event[1] == 1:
            current_cars += 1
            occupied_places += event[2]
        elif event[1] == -1:
            current_cars -= 1
            occupied_places -= event[2]

        if occupied_places == n:
            min_cars = min(min_cars, current_cars)

    return min_cars
