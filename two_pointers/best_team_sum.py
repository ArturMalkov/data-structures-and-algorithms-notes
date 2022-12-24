# players are already sorted
def best_team_sum(players: list[int]) -> int:

    best_sum = 0

    for best_player in range(len(players)-1, -1, -1):
        team_power = players[best_player]
        weakest_player = best_player - 1

        while weakest_player >= 0 and (players[weakest_player] + players[weakest_player - 1]) >= players[best_player]:
            team_power += players[weakest_player] + players[weakest_player - 1]
            weakest_player -= 1

        best_sum = max(best_sum, team_power)

    return best_sum


print(best_team_sum([1, 1, 3, 4, 6, 11]))


# another approach
def best_team_sum(players: list[int]) -> int:
    best_sum = 0

    for first in range(len(players)):
        last = first + 2
        current_sum = players[first]
        while last < len(players) and (last == first or players[first] + players[last-1] >= players[last]):
            current_sum += players[last-1] + players[last]
            last += 1
        best_sum = max(best_sum, current_sum)

    return best_sum


print(best_team_sum([1, 1, 3, 4, 6, 11]))
