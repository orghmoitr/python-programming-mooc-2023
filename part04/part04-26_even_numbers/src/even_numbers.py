# Write your solution here

def even_numbers(my_list: list) -> list:
    list_of_evens = []
    for item in my_list:
        if item % 2 == 0:
            list_of_evens.append(item)
    return list_of_evens

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
