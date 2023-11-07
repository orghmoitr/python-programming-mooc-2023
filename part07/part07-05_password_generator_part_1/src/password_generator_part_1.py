# Write your solution here

from random import choice
from string import ascii_lowercase

def generate_password(length: int) -> str:
    string = ""
    for i in range(length):
        string += choice(ascii_lowercase)
    return string

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
