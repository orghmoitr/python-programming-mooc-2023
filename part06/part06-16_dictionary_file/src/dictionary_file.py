# Write your solution here

def search_word():
    search_term = input("Search term: ")
    with open("dictionary.txt") as dictionary_file:
        dictionary = {}
        for line in dictionary_file:
            line = line.strip()
            parts = line.split("-")
            finnish_word = parts[0].strip()
            english_word = parts[1].strip()
            dictionary[finnish_word] = english_word
    for finnish_word, english_word in dictionary.items():
        if search_term in finnish_word or search_term in english_word:
            print(f"{finnish_word} - {english_word}")

def add_word():
    dictionary = {}
    finnish_word = input("The word in Finnish: ")
    english_word = input("The word in English: ")
    if finnish_word not in dictionary:
        dictionary[finnish_word] = english_word
    with open("dictionary.txt", "a") as dictionary_file:
        dictionary_file.write(f"{finnish_word} - {english_word}\n")
    print("Dictionary entry added")

def main():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        command = int(input("Function: "))
        if command == 1:
            add_word()
        elif command == 2:
            search_word()
        elif command == 3:
            print("Bye!")
            break

main()
