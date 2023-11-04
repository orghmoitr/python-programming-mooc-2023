# Write your solution here

if True:
    student_info = input("Student information: ")
    exercises_completed = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_info = input("Course information: ")
else:
    student_info = "students1.csv"
    exercises_completed = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"

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

courses = []
with open(course_info) as course_file:
    for line in course_file:
        line = line.strip()
        parts = line.split(":")
        courses.append(parts[1].strip())

with open("results.txt", "w") as results_file:
    results_file.write(f"{courses[0]}, {courses[1]} credits\n")
    results_file.write("======================================\n")
    results_file.write(f"name{' ':26}exec_nbr{' ':2}exec_pts.{' ':1}exm_pts.{' ':2}tot_pts.{' ':2}grade{' ':5}\n")
    for id, name in students.items():
        results_file.write(f"{name:30}{sum(exercises[id]):<10}{sum(exercises[id])//4:<10}{sum(exams[id]):<10}{(sum(exercises[id])//4)+sum(exams[id]):<10}{grades[id]:<10}\n")

with open("results.csv", "w") as results_file:
    for id, name in students.items():
        results_file.write(f"{id};{name};{grades[id]}\n")
