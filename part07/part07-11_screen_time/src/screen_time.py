# Write your solution here

from datetime import datetime, timedelta

if True:
    filename = input("Filename" )
    start_date = input("Start date: ")
    days = int(input("How many days: "))
else:
    filename = "late_june.txt"
    start_date = "24.6.2020"
    days = 5

start_time = datetime.strptime(start_date, "%d.%m.%Y")
    
print(f"Please type in screen time in minutes on each day (TV computer mobile):")

time_sum = 0
times = []
times_tv = []
times_computer = []
times_mobile = []

for i in range(days):
    new_time = (start_time + timedelta(days=i)).strftime('%d.%m.%Y')
    times.append(new_time)
    time_spent = input(f"Screen time {new_time}: ")
    time_tv = int(time_spent.split(" ")[0])
    time_computer = int(time_spent.split(" ")[1])
    time_mobile = int(time_spent.split(" ")[2])
    times_tv.append(time_tv)
    times_computer.append(time_computer)
    times_mobile.append(time_mobile)
    time_sum += time_tv + time_computer + time_mobile

with open(filename, "w") as my_file:
    my_file.write(f"Time period: {times[0]}-{times[len(times)-1]}\n")
    my_file.write(f"Total minutes: {time_sum}\n")
    my_file.write(f"Average minutes: {time_sum/days}\n")
    for i in range(len(times)):
        my_file.write(f"{times[i]}: {times_tv[i]}/{times_computer[i]}/{times_mobile[i]}\n")

