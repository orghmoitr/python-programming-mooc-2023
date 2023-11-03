# Write your solution here

def invert(dictionary: dict):
    my_dict = {}
    for key, value in dictionary.items():
        my_dict[value] = key
    dictionary.clear()
    for key, value in my_dict.items():
        dictionary[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
