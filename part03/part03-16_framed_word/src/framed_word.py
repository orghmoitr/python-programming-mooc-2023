# Write your solution here

word = input("Word: ")

print("*" * 30)
if len(word) % 2 != 0:
    spaces = (28 - len(word)) // 2
    print("*" + " " * spaces + word + " " * (spaces + 1) + "*")
else:
    spaces = (28 - len(word)) // 2
    print("*" + " " * spaces + word + " " * spaces + "*")
print("*" * 30)
