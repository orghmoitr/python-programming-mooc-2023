# Write your solution here

points = int(input("How many points [0-100]: "))

if points < 0:
    print("Grade: impossible!")
elif points < 50:
    print("Grade: fail")
elif points < 60:
    print("Grade: 1")
elif points < 70:
    print("Grade: 2")
elif points < 80:
    print("Grade: 3")
elif points < 90:
    print("Grade: 4")
elif points <= 100:
    print("Grade: 5")
else:
    print("Grade: impossible!")
