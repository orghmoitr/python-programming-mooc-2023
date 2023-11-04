# Write your solution here

who = input("Whom should I sign this to: ")
where = input("Where shall I save it: ")

with open(where, "w") as my_file:
    my_file.write(f"Hi {who}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
