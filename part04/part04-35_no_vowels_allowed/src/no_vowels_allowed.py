# Write your solution here

def no_vowels(string: str) -> str:
    new_string = ""
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            new_string += ""
        else:
            new_string += char
    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
