# Write your solution here

my_list = []

items = int(input("How many items: "))

i = 1
while i <= items:
    item = int(input(f"Item {i}: "))
    my_list.append(item)
    i += 1

print(my_list)
