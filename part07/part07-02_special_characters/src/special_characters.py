# Write your solution here

import string

def separate_characters(my_string: str) -> tuple:
    letters = ""
    punctuation = ""
    others = ""
    for i in range(len(my_string)):
        if my_string[i] in string.ascii_letters:
            letters += my_string[i]
        elif my_string[i] in string.punctuation:
            punctuation += my_string[i]
        else:
            others += my_string[i]
    return letters, punctuation, others

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
