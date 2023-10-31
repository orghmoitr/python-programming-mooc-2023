# Write your solution here

students = int(input("How many students on the course"))
group_size = int(input("Desired group size? "))

print(f"Number of groups formed: {(students + group_size - 1) // group_size}")
