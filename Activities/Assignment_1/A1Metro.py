# metroID, stationNum, direction, passTotal,
import random


class A1Metro:
    # metro_id = random.randrange(1, 1000)
    # station_num = 0
    # direction = "East"
    # pass_total = 0

    def __init__(self):
        # pass
        # self.metro_id = metro_id
        self.metro_id = random.randrange(1, 1000)
        self.station_num = 0
        self.direction = "East"
        self.pass_total = 0

    def default_values(self, metro_id):
        self.metro_id = metro_id
        print("Metro id is ", self.metro_id)
        print(
            f"Station number is {self.station_num}, direction {self.direction} and total passenger are "
            f"{self.pass_total}")


station_total = int(input("Enter the station "))

while station_total < 3:
    print("Enter more than 3")
    station_total = int(input("Enter the station "))

station_name = []
for i in range(0, station_total):
    station_name.append(input(f"Enter name of station {i + 1}: "))

train = A1Metro()

print("Metro id is ", train.metro_id)
print(f"Station number is {train.station_num}, direction {train.direction} and total passenger are {train.pass_total}")

train.default_values(random.randrange(1, 1000))
