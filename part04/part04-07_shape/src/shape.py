# Copy here code of line function from previous exercise and use it in your solution

def line(integer, string):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)

def shape(size1, char1, size2, char2):
    i = 1
    height = size1
    while i <= size1:
        line(i, char1)
        i += 1
    while size2 > 0:
        line(height, char2)
        size2 -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")

