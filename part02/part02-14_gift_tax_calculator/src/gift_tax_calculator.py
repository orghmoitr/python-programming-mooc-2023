# Write your solution here

gift_value = int(input("Value of gift: "))

if gift_value < 5000:
    print("No tax!")
elif gift_value < 25000:
    print(f"Amount of tax: {(100 + (gift_value - 5000) * 0.08)} euros")
elif gift_value < 55000:
    print(f"Amount of tax: {(1700 + (gift_value - 25000) * 0.10)} euros")
elif gift_value < 200000:
    print(f"Amount of tax: {(4700 + (gift_value - 55000) * 0.12)} euros")
elif gift_value < 1000000:
    print(f"Amount of tax: {(22100 + (gift_value - 200000) * 0.15)} euros")
else:
    print(f"Amount of tax: {(142100 + (gift_value - 1000000) * 0.17)} euros")
