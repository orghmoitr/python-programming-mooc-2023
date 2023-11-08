# Write your solution here

import json
import urllib.request

def retrieve_all() -> tuple:
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = json.loads(my_request.read())
    active = []
    for course in courses:
        if course["enabled"]:
            active.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
    return active

def retrieve_course(course_name: str) -> dict:
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    courses = json.loads(my_request.read())
    my_dict = {}
    my_dict["weeks"] = len(courses)
    max_students = 0
    hour_totals = 0
    exercise_totals = 0
    for course in courses:
        if int(courses[course]["students"]) > max_students:
            max_students = int(courses[course]["students"])
        hour_totals += int(courses[course]["hour_total"])
        exercise_totals += int(courses[course]["exercise_total"])
    my_dict["students"] = max_students
    my_dict["hours"] = hour_totals
    my_dict["hours_average"] = int(hour_totals / max_students)
    my_dict["exercises"] = exercise_totals
    my_dict["exercises_average"] = int(exercise_totals / max_students)
    return my_dict

# print(retrieve_course("ohtus17"))
