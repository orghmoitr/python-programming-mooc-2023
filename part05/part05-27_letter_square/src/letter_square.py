# Write your solution here

layers = int(input("Layers: "))

size = (ord('A')-1)+layers

for i in range(size, ord('A')-1, -1):
    for j in range(size, ord('A')-1, -1):
        if j > i:
            print(chr(j), end="")
        else:
            print(chr(i), end="")
    for j in range(ord('A')+1, size+1):
        if j > i:
            print(chr(j), end="")
        else:
            print(chr(i), end="")
    print()
for i in range(ord('A')+1, size+1):
    for j in range(size, ord('A')-1, -1):
        if j > i:
            print(chr(j), end="")
        else:
            print(chr(i), end="")
    for j in range(ord('A')+1, size+1):
        if j > i:
            print(chr(j), end="")
        else:
            print(chr(i), end="")
    print()
