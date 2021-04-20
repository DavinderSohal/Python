import random


class Train:
    def __init__(self):
        self.metro_id = random.randrange(1, 1000)
        self.station_no = 0
        self.direction = ['east', 'west']
        self.pass_total = 0

    # def __init__(self,metro_id):
    # 	self.metro_id = metro_id

    def get_metro_id(self):
        return self.metro_id

    def set_metro_id(self, metro_id):
        self.metro_id = metro_id

    def get_station_no(self):
        return self.station_no

    def set_station_no(self, station_no):
        self.station_no = station_no

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_pass_total(self):
        return self.pass_total

    def set_pass_total(self, pass_total):
        self.pass_total = pass_total

    def next_station(self, last_station):
        return self.station_no, last_station

    def __str__(self):
        return ("Metro Id " + str(self.metro_id) + "  Station No. " + str(self.station_no) + " Direction " + str(
            self.direction) + "Total Passengers in Train: " + str(self.pass_total))


def get_on_pass():
    return random.randrange(300)


def get_off_pass(passenger):
    if passenger == 0:
        return 0
    else:
        return random.randrange(passenger)


def calculate1(station_total):
    obj = Train()
    for station in range(station_total):
        print("\n-----------------------------------------------")
        if station == 0:
            waiting_passengers = get_on_pass()
            get_of = 0
            obj.pass_total = obj.pass_total - get_of
            if waiting_passengers > 250:
                left_passengers = waiting_passengers - 250
                obj.pass_total = 250
                aboard = 250
            else:
                obj.pass_total = waiting_passengers
                aboard = waiting_passengers
                left_passengers = 0
            print(f"New passengers waiting: {waiting_passengers}")
            print(f"Passengers left from last time: 0")
            print("----------------------------------")
            print(f"Train no. {obj.metro_id} leaving station {station + 1} with {obj.pass_total} passenger(s)")
            print(f'No. of passenger getting off from train : {get_of}')
            print(f'No. of new passenger waiting to board  : {waiting_passengers}')
            print(f"Passengers got on: {aboard}")
            print(f"Passengers left behind for next train: {left_passengers}")
        elif station == station_total - 1:
            waiting_passengers = 0
            get_of = obj.pass_total
            obj.pass_total = 0
            left_passengers = 0
            aboard = 0
            print(f"New passengers waiting: {waiting_passengers}")
            print(f"Passengers left from last time: 0")
            print("----------------------------------")
            print(f"Train no. {obj.metro_id} leaving station {station + 1} with {obj.pass_total} passenger(s)")
            print(f'No. of passenger getting off from train : {get_of}')
            print(f'No. of new passenger waiting to board  : {waiting_passengers}')
            print(f"Passengers got on: {aboard}")
            print(f"Passengers left behind for next train: {left_passengers}")
        else:
            waiting_passengers = get_on_pass()
            get_of = get_off_pass(obj.pass_total)
            obj.pass_total -= get_of
            if waiting_passengers + obj.pass_total > 250:
                left_passengers = waiting_passengers + obj.pass_total - 250
                aboard = waiting_passengers - left_passengers
                obj.pass_total += aboard
            else:
                obj.pass_total += waiting_passengers
                aboard = waiting_passengers
                left_passengers = 0
            print(f"New passengers waiting: {waiting_passengers}")
            print(f"Passengers left from last time: 0")
            print("----------------------------------")
            print(f"Train no. {obj.metro_id} leaving station {station + 1} with {obj.pass_total} passenger(s)")
            print(f'No. of passenger getting off from train : {get_of}')
            print(f'No. of new passenger waiting to board  : {waiting_passengers}')
            print(f"Passengers got on: {aboard}")
            print(f"Passengers left behind for next train: {left_passengers}")

        choose = input(
            f"\nDo you want to continue following Metro train {obj.metro_id}?\nType 'y' or 'Y' for yes, anything else "
            f"for no: ")
        if choose.lower() == "y":
            if station == station_total - 1:
                calculate2(station_total)
            else:
                continue
        else:
            break


def calculate2(station_total):
    obj = Train()
    for station in range(station_total, 0, -1):
        print("\n-----------------------------------------------")
        if station == station_total:
            waiting_passengers = get_on_pass()
            get_of = 0
            obj.pass_total = obj.pass_total - get_of
            if waiting_passengers > 250:
                left_passengers = waiting_passengers - 250
                obj.pass_total = 250
                aboard = 250
            else:
                obj.pass_total = waiting_passengers
                aboard = waiting_passengers
                left_passengers = 0
            print(f"New passengers waiting: {waiting_passengers}")
            print(f"Passengers left from last time: 0")
            print("----------------------------------")
            print(f"Train no. {obj.metro_id} leaving station {station} with {obj.pass_total} passenger(s)")
            print(f'No. of passenger getting off from train : {get_of}')
            print(f'No. of new passenger waiting to board  : {waiting_passengers}')
            print(f"Passengers got on: {aboard}")
            print(f"Passengers left behind for next train: {left_passengers}")
        elif station == 1:
            waiting_passengers = 0
            get_of = obj.pass_total
            obj.pass_total = 0
            left_passengers = 0
            aboard = 0
            print(f"New passengers waiting: {waiting_passengers}")
            print(f"Passengers left from last time: 0")
            print("----------------------------------")
            print(f"Train no. {obj.metro_id} leaving station {station} with {obj.pass_total} passenger(s)")
            print(f'No. of passenger getting off from train : {get_of}')
            print(f'No. of new passenger waiting to board  : {waiting_passengers}')
            print(f"Passengers got on: {aboard}")
            print(f"Passengers left behind for next train: {left_passengers}")
        else:
            waiting_passengers = get_on_pass()
            get_of = get_off_pass(obj.pass_total)
            obj.pass_total -= get_of
            if waiting_passengers + obj.pass_total > 250:
                left_passengers = waiting_passengers + obj.pass_total - 250
                aboard = waiting_passengers - left_passengers
                obj.pass_total += aboard
            else:
                obj.pass_total += waiting_passengers
                aboard = waiting_passengers
                left_passengers = 0
            print(f"New passengers waiting: {waiting_passengers}")
            print(f"Passengers left from last time: 0")
            print("----------------------------------")
            print(f"Train no. {obj.metro_id} leaving station {station} with {obj.pass_total} passenger(s)")
            print(f'No. of passenger getting off from train : {get_of}')
            print(f'No. of new passenger waiting to board  : {waiting_passengers}')
            print(f"Passengers got on: {aboard}")
            print(f"Passengers left behind for next train: {left_passengers}")

        choose = input(
            f"\nDo you want to continue following Metro train {obj.metro_id}?\nType 'y' or 'Y' for yes, anything else "
            f"for no: ")
        if choose.lower() == "y":
            if station == 1:
                calculate1(station_total)
            else:
                continue
        else:
            break


def main():
    print("Welcome !!")
    stations = int(input(" Enter the number of metro Stations (minimum 3) : "))
    while stations < 3:
        stations = int(input(" Enter the number of metro Stations (minimum 3) : "))

    station_name = []
    for i in range(stations):
        station_name.append(input(f"Enter the name of station {i + 1}: "))
    return stations


station_main = main()
calculate1(station_main)
print("\nThank you for using this program")
