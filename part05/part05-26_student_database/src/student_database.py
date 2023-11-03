# Write your solution here


def best_average_grade(students: dict) -> tuple:
    best_average = 0
    best_average_student = ""
    for student in students:
        sum_grade = 0
        for course_data in students[student]:
            sum_grade += course_data[1]
        average_grade = sum_grade / len(students[student])
        if best_average < average_grade:
            best_average = average_grade
            best_average_student = student
    return best_average, best_average_student
    

def most_courses_completed(students: dict) -> tuple:
    most_courses = 0
    most_courses_student = ""
    for student in students:
        if len(students[student]) > most_courses:
            most_courses = len(students[student])
            most_courses_student = student
    return most_courses, most_courses_student
            

def summary(students: dict):
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses_completed(students)[0]} {most_courses_completed(students)[1]}")
    print(f"best average grade {best_average_grade(students)[0]} {best_average_grade(students)[1]}")
    
    
def add_course(students: dict, name: str, course_data: tuple):
    if name in students:
        if course_data[1] > 0:
            if len(students[name]) == 0:
                students[name].append(course_data)
            else:
                match_found = False
                for course_info in students[name]:
                    if course_info[0] == course_data[0] and course_info[1] > course_data[1]:
                        match_found = True
                        break
                    if course_info[0] == course_data[0] and course_info[1] < course_data[1]:
                        match_found = True
                        students[name].remove(course_info)
                        students[name].append(course_data)
                        break
                if not match_found:
                    students[name].append(course_data)
                    

def average_grade(course_data: tuple) -> float:
    sum_grade = 0
    for data in course_data:
        sum_grade += data[1]
    return sum_grade / len(course_data)
        

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}: ")
        if len(students[name]) == 0:
            print(f" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            for data in students[name]:
                print(f"  {data[0]} {data[1]}")
            print(f" average grade {average_grade(students[name])}")

def add_student(students: dict, name: str):
    if name not in students:
        students[name] = []

            
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 5))
    print(students)
    summary(students)
