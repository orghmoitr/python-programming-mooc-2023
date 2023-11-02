# Write your solution here

my_list = []

i = 1
while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove, or e(x)it: ")
    if choice == "x":
        break
    elif choice == "d":
        my_list.append(i)
        i += 1
    elif choice == "r":
        my_list.pop(len(my_list)-1)
        i -= 1
print("Bye!")
