# Write your solution here

from random import choice, randint
from string import ascii_lowercase, digits

def add_char(passwd:str, charlist: str) -> str:
    passwd += choice(charlist)
    return passwd

def generate_strong_password(length: int, arg1: bool, arg2: bool) -> str:
    passwd = ""
    passwd = choice(ascii_lowercase)
    charlist = ascii_lowercase
    if arg1:
        passwd = add_char(passwd, digits)
        charlist += digits
    if arg2:
        special_chars = "!?=+-()#"
        passwd = add_char(passwd, special_chars)
        charlist += special_chars
    while len(passwd) < length:
        passwd = add_char(passwd, charlist)
    return passwd

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
