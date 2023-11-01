# Write your solution here

num = int(input("Please type in a number: "))

i = 0
while i < num // 2:
    print(i+1)
    print(num-i)
    i += 1
if num % 2 != 0:
    print(i+1)
