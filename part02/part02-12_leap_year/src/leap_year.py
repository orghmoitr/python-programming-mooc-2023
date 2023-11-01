# Write your solution here

year = int(input("Please type in a year: "))

leap_year = False

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        leap_year = False
    else:
        leap_year = True

if leap_year == True:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
