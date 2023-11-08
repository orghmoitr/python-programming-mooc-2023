# Write your solution here

from datetime import datetime, timedelta
import csv

def final_points() -> dict:
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

    final_points = {}
    for student in students:
        total_points = 0
        tasks = students[student]["stats"]["task"]
        points = students[student]["stats"]["points"]
        start_time = students[student]["start_time"]
        submission_time = students[student]["stats"]["submission_time"]
        for i in range(1, 9):
            max_points = 0
            for j in range(len(tasks)):
                if i == tasks[j] and submission_time[j] <= (start_time + timedelta(hours=3)):
                    if points[j] > max_points:
                        max_points = points[j]
            total_points += max_points
        final_points[student] = total_points

    return final_points
