# Write your solution here

from fractions import Fraction

def fractionate(amount: int) -> list:
    lst = []
    for i in range(1, amount+1):
        lst.append(Fraction(1, amount))
    return lst

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    print()
    print(fractionate(5))
