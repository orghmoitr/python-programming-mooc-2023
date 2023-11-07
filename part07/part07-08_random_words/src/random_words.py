# Write your solution here

from random import sample

def words(n: int, beginning: str) -> list:
    with open("words.txt") as word_file:
        word_list = []
        for word in word_file:
            word = word.strip()
            if word.startswith(beginning):
                word_list.append(word)
    return sample(word_list, n)
                
if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
