# Write your solution here

limit = int(input("Upper limit: "))

i = 1
result = 1
while result <= limit:
    print(result)
    result = 2 ** i
    i += 1
