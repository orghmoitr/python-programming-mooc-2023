# Write your solution here

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break
    product = 1
    fact = num
    while fact > 0:
        product *= fact
        fact -= 1
    print(f"The factorial of the number {num} is {product}")
print("Thanks and bye!")
