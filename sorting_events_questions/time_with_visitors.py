"""
N users visited a website. For each user its login (In) and logout time (Out) are known (intervals are inclusive).
What's the total time a website had at least one visitor?
"""


def get_time_with_visitors(num_visitors: int, time_in: list[float], time_out: list[float]) -> float:
    events = []

    for i in range(num_visitors):
        events.append((time_in[i], -1))
        events.append((time_out[i], -1))

    events.sort()
    visitors_online = 0
    time_with_visitors = 0

    for i in range(len(events)):
        if visitors_online > 0:
            time_with_visitors += events[i][0] - events[i-1][0]
            
        if events[i][1] == -1:
            visitors_online += 1
        else:
            visitors_online -= 1

    return time_with_visitors
