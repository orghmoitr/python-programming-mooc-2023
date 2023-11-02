# Write your solution here

def same_chars(string, integer1, integer2):
    if integer1 >= len(string) or integer2 >= len(string):
        return False
    return string[integer1] == string[integer2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False
    
    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False

