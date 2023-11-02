# Write your solution here

def list_of_stars(my_list: list):
    for i in range(len(my_list)):
        print("*" * my_list[i])

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
