# Write your solution here

from difflib import get_close_matches

text = input("Write text: ")

words = []
with open("wordlist.txt") as word_file:
    for word in word_file:
        word = word.strip()
        words.append(word)

textwords = text.split(" ")
newwords = []
misspelled_words = []
for word in textwords:
    if word.lower() in words:
        newwords.append(word)
    else:
        misspelled_words.append(word)
        newwords.append(f"*{word}*")

for i in range(len(newwords)):
    if i == len(newwords)-1:
        print(f"{newwords[i]}")
    else:
        print(f"{newwords[i]} ", end="")

print("suggestions:")
for word in misspelled_words:
    print(f"{word}: ", end="")
    close_matches = get_close_matches(word, words)
    for i in range(len(close_matches)):
        if i == len(close_matches)-1:
            print(f"{close_matches[i]}")
        else:
            print(f"{close_matches[i]}, ", end="")
