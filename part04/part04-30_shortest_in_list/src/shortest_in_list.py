# Write your solution here

def shortest(my_list: list) -> str:
    shortest = my_list[0]
    for string in my_list:
        if len(string) < len(shortest):
            shortest = string
    return shortest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    
    result = shortest(my_list)
    print(result)
