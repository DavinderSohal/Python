# -----------------------------------------------------
# A1 Metro
# Written by: Davinder Singh (2092836) and Navneet Kaur (2092453)
# This program will controls metro trains and keep track of stations and who gets on and off
# For this program we used constructor, accessor and mutator methods. This will tell the current location of the
# metro along with other details like number of passengers it's carrying, passengers getting off and boarding etc.
# -----------------------------------------------------

import random


def welcome():
    """this function will take input from user for number of stations, their names and the direction"""

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
                             "\n\tType  anything else 'East-West'"
                             "\nEnter your choice here: ")
    print()
    name_of_stations = {}
    for i in range(no_of_stations):
        name_of_stations[i + 1] = (input(f"Enter name of station {i + 1}: "))

    return no_of_stations, name_of_stations, choose_direction


class A1Metro:

    def __init__(self, metro_id = 1001):
        """created a constructor to initialize the values"""
        if metro_id == 1001:
            self.metro_id = random.randrange(1, 1000)
        else:
            self.metro_id = metro_id
        self.station_num = 0
        self.direction = 0
        self.pass_total = 0

    def get_metro_id(self):
        """Accessor method of metroID attribute."""
        return self.metro_id

    def get_station_num(self):
        """Accessor method of stationNum attribute."""
        return self.station_num

    def get_direction(self):
        """Accessor method of direction attribute."""
        return self.direction

    def get_pass_total(self):
        """Accessor method of passTotal attribute."""
        return self.pass_total

    def set_metro_id(self, metro_id):
        """Mutator method of metroID attribute."""
        self.metro_id = metro_id

    def set_station_num(self, station_num):
        """Mutator method of stationNum attribute."""
        self.station_num = station_num

    def set_direction(self, direction):
        """Mutator method of direction attribute."""
        self.direction = direction

    def set_pass_total(self, pass_total):
        """Mutator method of passTotal attribute."""
        self.pass_total = pass_total

    def change_station(self, total_station):
        """this method will be called when station # and direction of metro is to be changed"""
        global temp1
        global temp2
        global train_number
        if train_number == 1:
            temp = temp1
        else:
            temp = temp2
        # defining different conditions for changing the station and direction when required
        if self.station_num <= total_station:
            if self.station_num == total_station and self.direction == 0:
                self.direction = 1
            elif self.station_num == 1 and self.direction == 1:
                self.direction = 0
            if self.direction == 0:
                # using temp so that when train reach its final station then it will only change its direction but
                # the station number will remain same
                if temp == 1 and self.station_num == 1:
                    temp = 0
                else:
                    self.station_num += 1
            else:
                if temp == 0 and self.station_num == total_station:
                    temp = 1
                else:
                    self.station_num -= 1
            # changing train number
            if train_number == 1:
                temp1 = temp
                train_number = 2
            else:
                temp2 = temp
                train_number = 1

    def passengers(self):
        """this method will tell # of arriving passengers(generated randomly) and the passengers that got on board and
        those who are left behind"""

        # accessing the last_time dictionary to get the # of passengers that were left behind by the last train
        waiting_passengers = last_time.get(str(self.direction) + '-' + str(self.station_num), 0)
        new_passengers = 0
        pass_getting_off = 0
        pass_getting_on = 0

        # if train at its starting station there will be no passengers aboard, so, no passenger will be leaving the
        # train but only new ones will be arriving
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
        # when train is at its final station all the passengers will get off.
        elif (self.station_num == station_total and self.direction == 0) or (
                self.station_num == 1 and self.direction == 1):
            pass_getting_off = self.pass_total
            waiting_passengers = 0
        # for any other station than first and last one, this statement will be executed
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
        """this method will print the details about the metro"""
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
        # calling change_station method to change station number and the direction of train when necessary
        self.change_station(s_total)
        # calling passengers method to know the # of passengers on board, waiting and getting off.
        waiting_passengers, new_passengers, pass_getting_on, pass_getting_off = self.passengers()
        print(
            f"Metro {str(self.metro_id)} at Station number {str(self.station_num)}"
            f"\n(New passengers waiting {str(new_passengers)})"
            f"\n(Passengers left from last time "
            f"{last_time.get(str(self.direction) + '-' + str(self.station_num), 0)})")
        print("--------------------------")
        if train_number == 2:
            # we will not be keeping record of the passengers that are left behind by the second train and assigning
            # its value to zero
            last_time[str(self.direction) + "-" + str(self.station_num)] = 0
        else:
            last_time[str(self.direction) + "-" + str(self.station_num)] = waiting_passengers

        print(
            f"Metro {str(self.metro_id)} leaving station "
            f"{s_name[self.station_num]} {directions[self.direction]} bound "
            f"with {str(self.pass_total)} passenger(s)."
            f"\n\t  Passenger(s) got off: {str(pass_getting_off)}"
            f"\n\t  Passenger(s) new passengers waiting to board: {str(new_passengers)}"
            f"\n\t  Passenger(s) got on: {str(pass_getting_on)}"
            f"\n\t  Passenger(s) left behind waiting for next train: "
            f"{str(waiting_passengers)}")


# calling welcome function
station_total, station_name, required_direction = welcome()

# creating class objects and constructor is automatically called when object is created
train1 = A1Metro()
train2 = A1Metro()

print(f"\n ==> You will be following two metros with metro id {str(train1.metro_id)} and {str(train2.metro_id)}."
      f"\n ==> Both metros will be moving in same direction and metro {str(train2.metro_id)} will be following metro "
      f"{str(train1.metro_id)}.")

want_to_continue = True
start_second = False
temp1 = 0
temp2 = 0
train_number = 1
last_time = {}
while want_to_continue:
    if not start_second:
        # this block of code will run only once when train 1 is at station 1 and train 2 has not been started yet
        train1.display(station_name, station_total, required_direction.lower())
        start_second = True
    else:
        # making call to display method using objects that we created
        train1.display(station_name, station_total, required_direction.lower())
        train2.display(station_name, station_total, required_direction.lower())

    choice = input(
        f'\nDo you want to continue following Metro train {str(train1.metro_id)} and {str(train2.metro_id)}?'
        f'\nType "n" or "N" for no, anything else for yes: ')
    if choice.lower() == "n":
        want_to_continue = False
else:
    print(f"\n\n*********************************************\n"
          f"\n----[Thank you for using Metro Manager]----"
          f"\nBe sure to look out for future enhancements!"
          f"\n\n\t\t\t\t＼( ･_･)")

exit()
