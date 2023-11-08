# Write your solution here

import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    my_dict = json.loads(data)
    for hobby in my_dict:
        print(f"{hobby['name']} {hobby['age']} years (", end="")
        for i in range(len(hobby["hobbies"])):
            if i == len(hobby["hobbies"])-1:
                print(f"{hobby['hobbies'][i]}", end="")
            else:
                print(f"{hobby['hobbies'][i]}, ", end="")
        print(")")
