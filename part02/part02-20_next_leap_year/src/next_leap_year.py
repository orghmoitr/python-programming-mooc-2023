# Write your solution here

year = int(input("Year: "))

curr_year = year + 1
leap_year = False

while True:
    if curr_year % 4 == 0:
        if curr_year % 100 == 0 and curr_year % 400 != 0:
            leap_year = False
        else:
            leap_year = True
    if leap_year:
        break
    curr_year += 1
print(f"The next leap year after {year} is {curr_year}")
