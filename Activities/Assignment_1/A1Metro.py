import random


# colours = {'blue': '\033[94m', 'cyan': '\033[96m', 'green': '\033[92m',
#            'yellow': '\033[93m', 'red': '\033[91m', 'end': '\033[0m', 'bold': '\033[1m', 'underline': '\033[4m'}


def welcome():
    print("Welcome to Metro Manager - Enjoy your metro experience")
    print("------------------------------------------------------\n")
    no_of_stations = int(input("Enter number of metro stations (minimum 3): "))

    while no_of_stations < 3:
        print("Invalid Input\n")
        no_of_stations = int(input("Enter number of metro stations (minimum 3): "))

    print(f"This Metro line has {no_of_stations} stations.\n")

    choose_direction = input("Choose the direction."
                             "\n\tType (NS or ns) for 'North-South'"
                             "\n\tType (NE or ne) for 'North-East'"
                             "\n\tTYPE (NW or nw) for 'North-West'"
                             "\n\tType (SE or se) for 'South-East'"
                             "\n\tType (SW or sw) for 'South-West'"
                             "\n\tType anything else  'East-West'"
                             "\nEnter your choice here: ")
    name_of_stations = {}
    for i in range(no_of_stations):
        name_of_stations[i + 1] = (input(f"Enter name of station {i + 1}: "))

    return no_of_stations, name_of_stations, choose_direction


class A1Metro:

    def __init__(self, metro_id = 1001):
        if metro_id == 1001:
            self.metro_id = random.randrange(1, 1000)
        else:
            self.metro_id = metro_id
        self.station_num = 0
        self.direction = 0
        self.pass_total = 0

    def change_station(self, total_station):
        global temp1
        global temp2
        global train_number
        if train_number == 1:
            temp = temp1
        else:
            temp = temp2
        if self.station_num <= total_station:
            if self.station_num == total_station and self.direction == 0:
                self.direction = 1
            elif self.station_num == 1 and self.direction == 1:
                self.direction = 0
            if self.direction == 0:
                if temp == 1 and self.station_num == 1:
                    temp = 0
                else:
                    self.station_num += 1
            else:
                if temp == 0 and self.station_num == total_station:
                    temp = 1
                else:
                    self.station_num -= 1
            if train_number == 1:
                temp1 = temp
                train_number = 2
            else:
                temp2 = temp
                train_number = 1

    def passengers(self):
        waiting_passengers = last_time.get(str(self.direction) + '-' + str(self.station_num), 0)
        new_passengers = 0
        pass_getting_off = 0
        pass_getting_on = 0
        if (self.station_num == 1 and self.direction == 0) or (
                self.station_num == station_total and self.direction == 1):
            new_passengers = random.randrange(0, 300)
            if new_passengers <= 250:
                waiting_passengers = 0
                pass_getting_on = new_passengers
                self.pass_total = new_passengers
            else:
                waiting_passengers = new_passengers - 250
                pass_getting_on = 250
                self.pass_total = 250
        elif (self.station_num == station_total and self.direction == 0) or (
                self.station_num == 1 and self.direction == 1):
            pass_getting_off = self.pass_total
            waiting_passengers = 0
        else:
            new_passengers = random.randrange(0, 300)
            pass_getting_off = random.randrange(0, self.pass_total)
            self.pass_total -= pass_getting_off
            available_seats = 250 - self.pass_total
            if new_passengers + waiting_passengers <= available_seats:
                waiting_passengers = 0
                pass_getting_on = new_passengers + waiting_passengers
                self.pass_total += pass_getting_on
            else:
                waiting_passengers = (new_passengers + waiting_passengers) - available_seats
                pass_getting_on = available_seats
                self.pass_total = 250
        return waiting_passengers, new_passengers, pass_getting_on, pass_getting_off

    def display(self, s_name, s_total, user_direction):
        if user_direction == "ns":
            directions = ["north", "south"]
        elif user_direction == "ne":
            directions = ["north", "east"]
        elif user_direction == "nw":
            directions = ["north", "west"]
        elif user_direction == "se":
            directions = ["south", "east"]
        elif user_direction == "sw":
            directions = ["south", "west"]
        else:
            directions = ["east", "west"]

        print("\n------------------------------------------------------")
        self.change_station(s_total)
        waiting_passengers, new_passengers, pass_getting_on, pass_getting_off = self.passengers()
        print(
            f"Metro {self.metro_id} at Station number {self.station_num}"
            f"\n(New passengers waiting {new_passengers})"
            f"\n(Passengers left from last time "
            f"{last_time.get(str(self.direction) + '-' + str(self.station_num), 0)})")
        print("------------------------------------------------------")
        if train_number == 2:
            last_time[str(self.direction) + "-" + str(self.station_num)] = 0
        else:
            last_time[str(self.direction) + "-" + str(self.station_num)] = waiting_passengers

        print(
            f"Metro {self.metro_id} leaving station "
            f"{s_name[self.station_num]} {directions[self.direction]} bound "
            f"with {self.pass_total} passenger(s)."
            f"\n\t  Passenger(s) got off: {pass_getting_off}"
            f"\n\t  Passenger(s) new passengers waiting to board: {new_passengers}"
            f"\n\t  Passenger(s) got on: {pass_getting_on}"
            f"\n\t  Passenger(s) left behind waiting for next train: "
            f"{waiting_passengers}")


station_total, station_name, required_direction = welcome()

train1 = A1Metro()
train2 = A1Metro()

want_to_continue = True
start_second = False
temp1 = 0
temp2 = 0
train_number = 1
last_time = {}
while want_to_continue:
    if not start_second:
        train1.display(station_name, station_total, required_direction.lower())
        start_second = True
    else:
        train1.display(station_name, station_total, required_direction.lower())
        train2.display(station_name, station_total, required_direction.lower())

    choice = input(
        f'\nDo you want to continue following Metro train {train1.metro_id} and {train2.metro_id}?'
        f'\nType "y" or "Y" for yes, anything else for no: ')
    if choice.lower() != "y":
        want_to_continue = False
else:
    print(f"\n\n*********************************************\n"
          f"\n----[Thank you for using Metro Manager]----"
          f"\nBe sure to look out for future enhancements!"
          f"\n\n\t\t\t\t＼( ･_･)")

exit()
