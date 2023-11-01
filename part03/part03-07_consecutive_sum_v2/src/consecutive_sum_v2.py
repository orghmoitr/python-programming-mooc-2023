# Write your solution here

limit = int(input("Limit: "))

sum = 0
numbers = ""

i = 1
while sum < limit:
    sum += i
    if sum >= limit:
        numbers += f"{i}"
    else:
        numbers += f"{i} + "
    i += 1

print(f"The consecutive sum: {numbers} = {sum}")
