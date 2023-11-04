# wwite your solution here

if True:
    student_info = input("Student information: ")
    exercises_completed = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercises_completed = "exercises1.csv"
    exam_points = "exam_points1.csv"

students = {}
with open(student_info) as student_file:
    for line in student_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[int(parts[0])] = f"{parts[1]} {parts[2]}"

# print(f"students: {students}")
        
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

# print(f"exercises: {exercises}")
            
exams = {}
with open(exam_points) as exam_file:
    for line in exam_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[int(parts[0])] = []
        for exam in parts[1:]:
            exams[int(parts[0])].append(int(exam))

# print(f"exams: {exams}")
            
grades = {}
for id, name in students.items():
    if id in exercises and id in exams:
        total = (sum(exercises[id]) // 4) + (sum(exams[id]))
        if total < 15:
            grades[id] = 0
        elif total < 18:
            grades[id] = 1
        elif total < 21:
            grades[id] = 2
        elif total < 24:
            grades[id] = 3
        elif total < 28:
            grades[id] = 4
        else:
            grades[id] = 5

# print(f"grades: {grades}")
            
for id, name in students.items():
    if id in grades:
        print(f"{name} {grades[id]}")
