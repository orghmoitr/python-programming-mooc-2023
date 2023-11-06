# Write your solution here

def new_person(name: str, age: int) -> tuple:
    if name == "":
        raise ValueError("name cannot be an empty string")
    if len(name.split(" ")) < 2 or len(name) > 40:
        raise ValueError("name cannot contain less than 2 or more than 40 characters")
    if age < 0 or age > 150:
        raise ValueError("age cannot be less than 0 or greater than 150")
    return  name, age

if __name__ == "__main__":
    print(new_person("Andrew", 32))
