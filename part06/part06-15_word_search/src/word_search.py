# Write your solution here

def read_words_from_file() -> list:
    with open("words.txt") as word_file:
        words = []
        for word in word_file:
            words.append(word.strip())
    return words

def find_asterisk_words(words: list, search_term: str) -> list:
    wordlist = []
    for word in words:
        if "*" in search_term:
            i = search_term.find("*")
            if i == 0 and word.endswith(search_term[i+1:]):
                wordlist.append(word)
            elif i > 0 and word.startswith(search_term[:i]):
                wordlist.append(word)
    return wordlist

def find_dot_words(words: list, search_term: str) -> list:
    wordlist = []
    for word in words:
        found = True
        if "." in search_term and len(search_term) == len(word):
            for i in range(len(search_term)):
                if search_term[i] != "." and search_term[i] != word[i]:
                    found = False
                    break
            if found:
                wordlist.append(word)
    return wordlist

def find_similar_words(words: list, search_term: str) -> list:
    wordlist = []
    for word in words:
        if search_term == word:
            wordlist.append(word)
    return wordlist

def find_words(search_term: str) -> list:
    words = read_words_from_file()
    if "*" in search_term:
        wordlist = find_asterisk_words(words, search_term)
    elif "." in search_term:
        wordlist = find_dot_words(words, search_term)
    else:
        wordlist = find_similar_words(words, search_term)
    return wordlist

if __name__ == "__main__":
    print(find_words("ca."))
