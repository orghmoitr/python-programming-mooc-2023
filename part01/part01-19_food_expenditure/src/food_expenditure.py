# Write your solution here

weekly_eatings = int(input("How many times do you eat at the student cafeteria? "))
price_of_lunch = float(input("The price of a typical student lunch? "))
weekly_groceries = float(input("How much money do you spend on groceries in a week? "))

weekly_expenditure = weekly_eatings * price_of_lunch + weekly_groceries

print()
print(f"Average food expenditure:")
print(f"Daily: {weekly_expenditure / 7} euros")
print(f"Weekly: {weekly_expenditure} euros")
