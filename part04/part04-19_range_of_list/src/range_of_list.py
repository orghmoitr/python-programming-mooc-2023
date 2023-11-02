# Write your solution here

def range_of_list(my_list: list) -> int:
    return max(my_list) - min(my_list)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)
