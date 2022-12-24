"""
N users visited a website. For each user its login (In) and logout time (Out) are known (intervals are inclusive).
Boss visited the website m times at boss_check_times.
Which results did the boss see?
"""


# my solution
def get_boss_check_results\
                (num_visitors: int, time_in: list[float], time_out: list[float], boss_check_times: list[float]) -> list[int]:
    events = []
    for i in range(num_visitors):
        events.append((time_in[i], -1))
        events.append((time_out[i], 1))
    events.sort()

    boss_check_results = []
    visitors_online = 0
    boss_check_number = 0

    for i in range(len(events)-1):
        if events[i][1] == -1:
            visitors_online += 1
        else:
            visitors_online -= 1

        if boss_check_number < len(boss_check_times) \
                and events[i][0] <= boss_check_times[boss_check_number] <= events[i+1][0]:
            boss_check_results.append(visitors_online)
            boss_check_number += 1

    return boss_check_results


# proposed approach
def get_boss_check_results(num_visitors: int,
                           time_in: list[float],
                           time_out: list[float],
                           num_checks: int,
                           boss_check_times: list[float]) -> list[int]:
    events = []
    for i in range(num_visitors):
        events.append((time_in[i], -1))
        events.append((time_out[i], 1))

    for i in range(num_checks):
        events.append((boss_check_times[i], 0))  # 0 indicates a new event - a boss' check

    events.sort()  # time complexity - O((N+M) * log(N+M)), where N is num_visitors and M is num_checks

    visitors_online = 0
    boss_check_results = []

    for event in events:
        if event[1] == -1:
            visitors_online += 1
        elif event[1] == 1:
            visitors_online -= 1
        else:  # if event[1] == 0, i.e. it's a boss' check
            boss_check_results.append(visitors_online)

    return boss_check_results
