# Write your solution here


def print_stars(grades: list, num: int):
    stars = ""
    for grade in grades:
        if num == grade:
            stars += "*"
    return stars


def print_grade_distribution(grades: list):
    print("Grade distribution:")
    i = 5
    while i >= 0:
        print(f"{i}: {print_stars(grades, i)}")
        i -= 1


def get_pass_percentage(exam_points: list, exercise_points: list) -> float:
    passed = 0
    for i in range(len(exam_points)):
        if exam_points[i] >= 10 and (exam_points[i]+exercise_points[i]) >= 15:
            passed += 1
    return (passed / len(exam_points)) * 100


def get_points_average(exam_points: list, exercise_points: list) -> float:
    sum_points = 0
    for i in range(len(exam_points)):
        sum_points += exam_points[i] + exercise_points[i]
    return sum_points / len(exam_points)


def get_grades(exam_points: list, exercise_points: list) -> list:
    grades = []
    for i in range(len(exam_points)):
        if exam_points[i] < 10:
            grade = 0
        else:
            if exam_points[i] + exercise_points[i] < 15:
                grade = 0
            elif exam_points[i] + exercise_points[i] < 18:
                grade = 1
            elif exam_points[i] + exercise_points[i] < 21:
                grade = 2
            elif exam_points[i] + exercise_points[i] < 24:
                grade = 3
            elif exam_points[i] + exercise_points[i] < 28:
                grade = 4
            else:
                grade = 5
        grades.append(grade)
    return grades
    

def get_exercise_points(exercises_completed: list) -> list:
    exercise_points = []
    for exercises in exercises_completed:
        exercise_points.append(exercises // 10)
    return exercise_points


def print_statistics(exam_points: list, exercises_completed: list):
    print("Statistics:")
    exercise_points = get_exercise_points(exercises_completed)
    grades = get_grades(exam_points, exercise_points)
    points_average = get_points_average(exam_points, exercise_points)
    print(f"Points average: {points_average:.1f}")
    pass_percentage = get_pass_percentage(exam_points, exercise_points)
    print(f"Pass percentage: {pass_percentage:.1f}")
    print_grade_distribution(grades)
    

def get_exercises_completed(inputs: list) -> list:
    exercises_completed = []
    for user_input in inputs:
        exercise_completed = user_input.split(" ")[1]
        exercises_completed.append(int(exercise_completed))
    return exercises_completed


def get_exam_points(inputs: list) -> list:
    exam_points = []
    for user_input in inputs:
        exam_point = user_input.split(" ")[0]
        exam_points.append(int(exam_point))
    return exam_points


def input_from_user() -> list:
    inputs = []
    while True:
        prompt = input("Exam points and exercises completed: ")
        if prompt == "":
            break
        inputs.append(prompt)
    return inputs


def main():
    inputs = input_from_user()
    exam_points = get_exam_points(inputs)
    exercises_completed = get_exercises_completed(inputs)
    print_statistics(exam_points, exercises_completed)

    
main()
