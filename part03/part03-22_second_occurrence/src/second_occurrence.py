# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index1 = -1
index2 = -1

index1 = string.find(substring)
while index1 != -1 and index1+len(substring) < len(string):
    index2 = string.find(substring, index1+len(substring))
    if index2 != -1:
        break
    index1 += 1

if index2 != -1:
    print(f"The second occurrence of the substring is at index {index2}.")
else:
    print(f"The substring does not occur twice in the string.")
