# Write your solution here

num = int(input("Please type in a number: "))

i = 2
while i <= num:
    print(i)
    print(i-1)
    i += 2
if num % 2 != 0:
    print(i-1)
