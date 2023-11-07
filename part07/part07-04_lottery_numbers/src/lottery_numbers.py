# Write your solution here

from random import randint, sample

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    lst = []
    while len(lst) != amount:
        number = randint(lower, upper)
        if number not in lst:
            lst.append(number)
    return sorted(lst)
    

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
