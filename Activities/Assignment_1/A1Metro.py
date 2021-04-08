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

    name_of_stations = {}
    for i in range(no_of_stations):
        name_of_stations[i + 1] = (input(f"Enter name of station {i + 1}: "))

    return no_of_stations, name_of_stations


class A1Metro:

    def __init__(self, metro_id = random.randrange(1, 1000)):
        self.metro_id = metro_id
        self.station_num = 0
        self.direction = 0
        self.pass_total = 0

    def change_station(self, total_station, temp):
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
            return temp, self.station_num

    def passengers(self, waiting_passengers):
        waiting_passengers = waiting_passengers.get(str(self.direction) + '-' + str(self.station_num), 0)
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

    def display(self, s_name, s_total):
        directions = ["east", "west", "north", "south"]
        want_to_continue = True
        temp = 0
        waiting_passengers = {}
        last_time = {}
        while want_to_continue:
            print("\n------------------------------------------------------\n")
            temp, self.station_num = self.change_station(s_total, temp)
            waiting_passengers[str(self.direction) + "-" + str(
                self.station_num)], new_passengers, pass_getting_on, pass_getting_off = self.passengers(
                waiting_passengers)
            print(
                f"Station number {self.station_num}"
                f"\n(New passengers waiting {new_passengers})"
                f"\n(Passengers left from last time "
                f"{last_time.get(str(self.direction) + '-' + str(self.station_num), 0)})")
            print("------------------------------------------------------")
            last_time[str(self.direction) + "-" + str(self.station_num)] = waiting_passengers[
                str(self.direction) + '-' + str(self.station_num)]

            print(
                f"Metro {self.metro_id} leaving station "
                f"{s_name[self.station_num]} {directions[self.direction]} bound "
                f"with {self.pass_total} passenger(s)."
                f"\n\t  Passenger(s) got off: {pass_getting_off}"
                f"\n\t  Passenger(s) new passengers waiting to board: {new_passengers}"
                f"\n\t  Passenger(s) got on: {pass_getting_on}"
                f"\n\t  Passenger(s) left behind waiting for next train: "
                f"{waiting_passengers[str(self.direction) + '-' + str(self.station_num)]}")

            choice = input(
                f'\nDo you want to continue following Metro train {self.metro_id}?'
                f'\nType "y" or "Y" for yes, anything else for no: ')
            if choice.lower() == "y":
                continue
            else:
                want_to_continue = False


station_total, station_name = welcome()

train = A1Metro()

train.display(station_name, station_total)

print(f"\n----[Thank you for using Metro Manager]----\nBe sure to look out for future enhancements!\n\n\t\t\t\t＼( ･_･)")

exit()
