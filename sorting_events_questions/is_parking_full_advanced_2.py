# A shopping mall has N parking places (from 1 to N). There were M cars in total, some of them occupied several consecutive
# parking places. We know arrival and departure time for each car + the number of parking places it occupied.
# Were there moments in time when all parking places were occupied?
# If yes, define the minimum number of cars at these moments and their registration numbers. If not, return empty list/set

# not optimized solution - see copying below
def min_cars_on_full_parking(n, cars):
    events = []

    for i in range(len(cars)):
        registration_number, arrival_time, departure_time, from_place, to_place = cars[i]
        events.append((arrival_time, 1, i, from_place - to_place + 1))
        events.append((departure_time, -1, i, from_place - to_place + 1))

    events.sort()

    occupied_places = 0
    current_cars = 0
    min_cars = len(cars) - 1
    current_registration_numbers = set()
    registration_numbers_at_peaks = set()

    for event in events:
        if event[1] == 1:
            current_cars += 1
            occupied_places += event[3]
            current_registration_numbers.add(event[2])
        elif event[1] == -1:
            current_cars -= 1
            occupied_places -= event[3]
            current_registration_numbers.remove(event[2])

        if occupied_places == n and current_cars < min_cars:
            min_cars = current_cars
            registration_numbers_at_peaks = current_registration_numbers.copy()  # copying may be O(M**2) time complexity if it's too frequent

    return registration_numbers_at_peaks


# optimized solution - 2 iterations
def min_cars_on_full_parking(cars, n):
    events = []

    for i in range(len(cars)):
        arrival_time, departure_time, from_place, to_place = cars[i]
        events.append((arrival_time, i, 1, (from_place - to_place + 1)))
        events.append((departure_time, i, -1, (from_place - to_place + 1)))

    # first iteration
    events.sort()
    occupied_places = 0
    min_cars = 0
    current_cars = 0

    for event in events:
        if event[2] == 1:
            current_cars += 1
            occupied_places += event[3]
        elif event[2] == -1:
            current_cars -= 1
            occupied_places -= event[3]

        if occupied_places == n and current_cars < min_cars:
            min_cars = current_cars

    # second iteration
    occupied_places = 0
    registration_numbers = set()
    current_cars = 0

    for event in events:
        if event[2] == 1:
            occupied_places += event[3]
            current_cars += 1
            registration_numbers.add(event[1])
        elif event[2] == -1:
            occupied_places -= event[3]
            current_cars -= 1
            registration_numbers.remove(event[1])

        if occupied_places == n and current_cars == min_cars:
            return registration_numbers  # we've avoided copying of registration_numbers

    return set()
