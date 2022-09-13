
from random import shuffle
import math


class Team:
    def __init__(self, p1: str, p2: str):
        self.players = [p1, p2]
        shuffle(self.players)

    def __str__(self):
        return f"<{self.players[0]}>-<{self.players[1]}>"


class Match:
    def __init__(self, t1: Team, t2: Team):
        self.teams = [t1, t2]
        shuffle(self.teams)

    def __str__(self):
        return f"{self.teams[0]} vs. {self.teams[1]}"


if __name__ == '__main__':
    # Constants that the user can change to adapt to league needs

    matches_per_player = 20

    num_players = 12

    max_retries = 100000

    # Algorithm starts here:

    # Names are given to each player

    Players = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")[0:num_players]

    shuffle(Players)

    # Creating all teams by enumerating all player pairs

    teams = []

    for p1 in range(0, len(Players)):
        for p2 in range(p1 + 1, len(Players)):
            teams.append(Team(Players[p1], Players[p2]))

    shuffle(teams)

    # Creating all different matches by enumerating all team pairs removing matches with the same player in both sides

    matches = []

    for t1 in range(0, len(teams)):
        for t2 in range(t1 + 1, len(teams)):
            if not teams[t1].players[0] in teams[t2].players and not teams[t1].players[1] in teams[t2].players:
                match = Match(teams[t1], teams[t2])

                matches.append(match)

    shuffle(matches)

    print(f"Players: {len(Players)}")

    print(f"Teams: {len(teams)}")

    print(f"Matches: {len(matches)}")

    # Searching for the best combination of matches that equalizes the number of matches for all players

    league_total_matches = int(matches_per_player * len(Players) / 4)

    best_worst_deviation = math.inf

    best_matches = None

    while max_retries > 0 and best_worst_deviation > 0:
        max_retries -= 1

        shuffle(matches)

        reduced_matches = matches[0:league_total_matches]

        num_matches_per_player = [0] * len(Players)

        for i, p in enumerate(Players):
            for m in reduced_matches:
                if p in m.teams[0].players or p in m.teams[1].players:
                    num_matches_per_player[i] += 1

        worst_deviation = 0

        typical_deviation = 0

        for i, p in enumerate(Players):
            deviation = abs(num_matches_per_player[i] - matches_per_player)

            typical_deviation += deviation

            calculated_deviation = deviation * 10000 + typical_deviation

            if calculated_deviation > worst_deviation:
                worst_deviation = calculated_deviation

        if worst_deviation < best_worst_deviation:
            best_worst_deviation = worst_deviation
            best_matches = reduced_matches
            best_num_matches_per_player = num_matches_per_player

            print(f"Found a better combination with fitness {best_worst_deviation}, pending retries {max_retries}")

    for t in best_matches:
        print(t)

    print(f"best_worst_deviation: {best_worst_deviation}")

    for i, p in enumerate(Players):
        print(f"Player: {p}, num matches: {best_num_matches_per_player[i]}")
