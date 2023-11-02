# Write your solution here

def all_the_longest(names: list) -> list:
    longest_list = []
    longest = names[0]
    length_of_longest = len(names[0])
    for name in names:
        if len(name) > len(longest):
            longest = name
            length_of_longest = len(name)
    for name in names:
        if len(name) == length_of_longest:
            longest_list.append(name)
    return longest_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
