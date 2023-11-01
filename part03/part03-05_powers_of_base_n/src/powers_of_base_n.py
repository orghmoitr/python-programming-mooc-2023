# Write your solution here

limit = int(input("Upper limit: "))
base = int(input("Base: "))

i = 1
result = 1
while result <= limit:
    print(result)
    result = base ** i
    i += 1
