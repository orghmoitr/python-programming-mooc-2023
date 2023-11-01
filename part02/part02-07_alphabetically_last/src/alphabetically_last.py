# Write your solution here

first_word = input("Please type in the 1st word: ")
second_word = input("Please type in the 2nd word: ")

if first_word > second_word:
    print(f"{first_word} comes alphabetically last.")
elif second_word > first_word:
    print(f"{second_word} comes alphabetically last.")
else:
    print("You gave the same word twice.")
