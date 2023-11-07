# Write your solution here

from random import choice

def play(die1: str, die2: str, times: int) -> tuple:
    wins_die1 = 0
    wins_die2 = 0
    for i in range(times):
        throw_die1 = roll(die1)
        throw_die2 = roll(die2)
        if throw_die1 > throw_die2:
            wins_die1 += 1
        elif throw_die2 > throw_die1:
            wins_die2 += 1
    ties = times - (wins_die1 + wins_die2)
    return wins_die1, wins_die2, ties

def roll(die: str) -> int:
    if die == "A":
        return choice([3, 3, 3, 3, 3, 6])
    elif die == "B":
        return choice([2, 2, 2, 5, 5, 5])
    elif die == "C":
        return choice ([1, 4, 4, 4, 4, 4])

if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
