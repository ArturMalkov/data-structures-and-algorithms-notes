"""
N users visited a website. For each user its login (In) and logout time (Out) are known (intervals are inclusive).
What's the maximum number of users logged in at the same time?
"""


# n is the total number of visitors, time_in is the list with login time for each user, time_out - list with logout time
# for each user. Indexes in these lists indicate the number of a visitor.
def get_max_users_online(n: int, time_in: list[float], time_out: list[float]) -> int:
    events = []
    for i in range(n):
        events.append((time_in[i], -1))  # -1 is an event type (must be less than time_out for it to appear first after sorting - in case login of one user coincides with logout of another user)
        events.append((time_out[i], 1))  # 1 is an event type

    events.sort()
    max_users_online = 0
    current_users_online = 0

    for event in events:
        if event[1] == -1:
            current_users_online += 1
        else:
            current_users_online -= 1
        max_users_online = max(max_users_online, current_users_online)

    return max_users_online
