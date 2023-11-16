class BallPlayer:

    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

# Write your solution here


def most_goals(ball_players: list):
    return max(ball_players, key=lambda ball_player: ball_player.goals).name


def most_points(ball_players: list):
    ball_player = max(ball_players, key=lambda ball_player: ball_player.goals + ball_player.passes)
    return ball_player.name, ball_player.number

def least_minutes(ball_players: list):
    return min(ball_players, key=lambda ball_player: ball_player.minutes)


if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)

    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))
