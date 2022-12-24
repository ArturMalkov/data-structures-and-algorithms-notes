# A shopping mall has N parking places (from 1 to N). There were M cars in total, some of them occupied several consecutive
# parking places. We know arrival and departure time for each car + the number of parking places it occupied.
# Was there a moment in time when all parking places were occupied?
def is_parking_full(cars, n):
    events = []

    for car in cars:
        arrival_time, departure_time, place_from, place_to = car
        events.append((arrival_time, 1, place_to - place_from + 1))
        events.append((departure_time, -1, place_to - place_from + 1))

    events.sort()
    places_occupied = 0

    for event in events:
        if event[1] == 1:
            places_occupied += event[2]
        elif event[1] == -1:
            places_occupied -= event[2]

        if places_occupied == n:
            return True

    return False
