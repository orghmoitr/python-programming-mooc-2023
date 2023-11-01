# Write your solution here

string = input("Please type in a string: ")

vowels = "aeo"

i = 0
while i < len(vowels):
    letter = vowels[i]
    if letter in string:
        print(f"{letter} found")
    else:
        print(f"{letter} not found")
    i += 1
