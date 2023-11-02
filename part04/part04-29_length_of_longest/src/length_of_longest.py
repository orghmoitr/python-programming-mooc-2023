# Write your solution here

def length_of_longest(my_list: list) -> int:
    longest = len(my_list[0])
    for i in range(len(my_list)):
        if len(my_list[i]) > longest:
            longest = len(my_list[i])
    return longest


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
