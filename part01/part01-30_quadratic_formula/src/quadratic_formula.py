# Write your solution here
# Let's take the square root of math-module in use

from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

pos_root = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
neg_root = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)

print(f"The roots are {pos_root} and {neg_root}")
