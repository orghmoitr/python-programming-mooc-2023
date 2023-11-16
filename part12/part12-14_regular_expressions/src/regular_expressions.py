# Write your solution here

import re


def is_dotw(my_string: str):
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    else:
        return False


def all_vowels(my_string: str):
    for char in my_string:
        if not re.search("[aeiou]", char, flags=re.IGNORECASE):
            return False
    return True


def time_of_day(my_string: str):
    if re.search("^([0-1][0-9]|[0-2][0-3]):([0-5][0-9]):([0-5][0-9])$", my_string):
        return True
    else:
        return False


if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    print(time_of_day("19:zz:04"))
    print(time_of_day("25:13:01"))
