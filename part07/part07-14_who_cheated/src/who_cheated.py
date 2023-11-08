# Write your solution here

from datetime import datetime, timedelta
import csv

def cheaters() -> list:
    students = {}
    with open("start_times.csv") as start_times_file:
        for line in csv.reader(start_times_file, delimiter=";"):
            name = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")
            students[name] = {
                "start_time": start_time,
                "stats": {
                    "task": [],
                    "points": [],
                    "submission_time": []
                }
            }

    with open("submissions.csv") as submissions_file:
        for line in csv.reader(submissions_file, delimiter=";"):
            student = line[0]
            task = int(line[1])
            points = int(line[2])
            submission_time = datetime.strptime(line[3], "%H:%M")
            students[student]["stats"]["task"].append(task)
            students[student]["stats"]["points"].append(points)
            students[student]["stats"]["submission_time"].append(submission_time)

    cheaters = []
    for student in students:
        time1 = students[student]["start_time"]
        time2 = students[student]["stats"]["submission_time"]
        for time in time2:
            if time > (time1 + timedelta(hours=3)):
                if student not in cheaters:
                    cheaters.append(student)

    return cheaters

# print(cheaters())
