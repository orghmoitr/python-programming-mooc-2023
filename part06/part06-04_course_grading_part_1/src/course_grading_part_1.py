# write your solution here

if True:
    student_info = input("Student information: ")
    exercises_completed = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercises_completed = "exercises1.csv"

students = {}
    
with open(student_info) as student_file:
    for line in student_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[int(parts[0])] = f"{parts[1]} {parts[2]}"

exercises = {}

with open(exercises_completed) as exercise_file:
    for line in exercise_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[int(parts[0])] = []
        for exercise in parts[1:]:
            exercises[int(parts[0])].append(int(exercise))

for id, name in students.items():
    if id in exercises:
        print(f"{name} {sum(exercises[id])}")

