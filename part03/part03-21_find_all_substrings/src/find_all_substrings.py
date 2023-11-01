# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

while True:
    index = word.find(char)
    if index == -1 or len(word) == 0:
        break
    elif index+3 <= len(word):
        print(word[index: index+3])
    word = word[index+1:]

