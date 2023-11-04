# Write your solution here

import math

def greatest_distance_from_one_station(stations: dict, station: str) -> tuple:
    station_list = []
    for station_name in stations:
        station_list.append(station_name)
    station_list.remove(station)

    station1 = ""
    station2 = ""
    greatest = 0.0
    for station_name in station_list:
        if distance(stations, station, station_name) > greatest:
            greatest = distance(stations, station, station_name)
            station1 = station
            station2 = station_name
    return station1, station2, greatest

def greatest_distance(stations: dict) -> tuple:
    desired_station1 = ""
    desired_station2 = ""
    desired_greatest = 0.0
    for station in stations:
        station1, station2, greatest = greatest_distance_from_one_station(stations, station)
        if greatest > desired_greatest:
            desired_station1 = station1
            desired_station2 = station2
            desired_greatest = greatest
    return desired_station1, desired_station2, desired_greatest


def distance(stations: dict, station1: str, station2: str) -> float:
    x_km = (float(stations[station1][0]) - float(stations[station2][0])) * 55.26
    y_km = (float(stations[station1][1]) - float(stations[station2][1])) * 111.2
    return math.sqrt(x_km**2 + y_km**2)
        
def get_station_data(filename: str) -> dict:
    with open(filename) as station_file:
        station_dict = {}
        for line in station_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            station_dict[parts[3]] = (float(parts[0]), float(parts[1]))
    return station_dict

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
