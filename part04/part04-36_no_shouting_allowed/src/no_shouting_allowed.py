# Write your solution here

def no_shouting(my_list: list) -> list:
    new_list = []
    for item in my_list:
        if item.isupper():
            continue
        new_list.append(item)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
