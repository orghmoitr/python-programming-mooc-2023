# write your solution here

text = input("Write text: ")

words = []
with open("wordlist.txt") as word_file:
    for word in word_file:
        word = word.strip()
        words.append(word)

textwords = text.split(" ")
newwords = []
for word in textwords:
    if word.lower() in words:
        newwords.append(word)
    else:
        newwords.append(f"*{word}*")

for i in range(len(newwords)):
    if i == len(newwords)-1:
        print(f"{newwords[i]}")
    else:
        print(f"{newwords[i]} ", end="")
