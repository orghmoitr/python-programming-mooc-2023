# WRITE YOUR SOLUTION HERE:

from string import punctuation


def read_from_file(filename: str):
    new_punctuation = ("".join([char for char in punctuation
                                if char != "-" and char != "'"]))
    string = ""
    with open(filename) as my_file:
        for line in my_file:
            line = line.strip()
            string += ("".join([c if c not in new_punctuation else " "
                                for c in line]))
    return string


def most_common_words(filename: str, lower_limit: int):
    string = read_from_file(filename)
    my_dict = {}
    for word in list(string.split(" ")):
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1
    return {w: my_dict[w] for w in my_dict
            if my_dict[w] >= lower_limit and w != ""}


if __name__ == "__main__":
    print(most_common_words("programming.txt", 6))
