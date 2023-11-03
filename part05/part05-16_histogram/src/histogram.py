# Write your solution here

def histogram(string):
    letter_list = list(string)

    groups = {}
    for letter in letter_list:
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(letter)

    for key, value in groups.items():
        print(f"{key} {'*' * len(value)}")

