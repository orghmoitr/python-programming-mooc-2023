# Write your solution here

def line(integer, string):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")
