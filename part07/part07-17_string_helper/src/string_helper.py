# Write your solution here

from string import ascii_lowercase, ascii_uppercase, digits, whitespace

def change_case(orig_string: str) -> str:
    new_string = ""
    for char in orig_string:
        if char in ascii_lowercase:
            new_string += char.upper()
        elif char in ascii_uppercase:
            new_string += char.lower()
        else:
            new_string += char
    return new_string

def split_in_half(orig_string: str) -> tuple:
    mid_index = len(orig_string) // 2
    return orig_string[:mid_index], orig_string[mid_index:]

def remove_special_characters(orig_string: str) -> str:
    new_string = ""
    for char in orig_string:
        if char in ascii_lowercase or char in ascii_uppercase or char in digits or char in whitespace:
            new_string += char
    return new_string

