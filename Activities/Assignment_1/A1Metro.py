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


def compare(metro_id1, metro_id2, current_station1, current_station2, next_station1, next_station2, pass_total1,
            pass_total2, direction1, direction2, count_metro1, count_metro2):
    """This function will return a table comparing different aspects of two trains"""

    print("\nCOMPARISON TABLE:\n")
    print(f"|-------------------------|---------------------|---------------------|"
          f"\n| Metro ID                |      Metro {str(metro_id1).zfill(3)}      |      Metro "
          f"{str(metro_id2).zfill(3)}      |"
          f"\n|-------------------------|---------------------|---------------------|"
          f"\n| Current Station         |    Station No. {str(current_station1).zfill(2)}   |   Station No. "
          f"{str(current_station2).zfill(2)}    |"
          f"\n|-------------------------|---------------------|---------------------|"
          f"\n| Next Station            |    Station No. {str(next_station1).zfill(2)}   |   Station No. "
          f"{str(next_station2).zfill(2)}    |"
          f"\n|-------------------------|---------------------|---------------------|"
          f"\n| Passengers Aboard       |         {str(pass_total1).zfill(3)}         |         "
          f"{str(pass_total2).zfill(3)}         |"
          f"\n|-------------------------|---------------------|---------------------|"
          f"\n| Direction               |         {direction1}       |        {direction2}        |"
          f"\n|-------------------------|---------------------|---------------------|"
          f"\n| # of stations travelled |         {str(count_metro1).zfill(2)}          |         "
          f"{str(count_metro2).zfill(2)}          |"
          f"\n|-------------------------|---------------------|---------------------|")


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

    def get_direction(self, u_direction):
        """Accessor method of direction attribute."""
        if u_direction == "ns":
            directions = ["North", "South"]
        elif u_direction == "ne":
            directions = ["North", "East "]
        elif u_direction == "nw":
            directions = ["North", "West "]
        elif u_direction == "se":
            directions = ["South", "East "]
        elif u_direction == "sw":
            directions = ["South", "West "]
        else:
            directions = ["East ", "West "]
        return directions[self.direction]

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
        # using global to access variable from outer scope
        global temp1
        global temp2
        global train_number
        if train_number == 1:
            temp = temp1
        else:
            temp = temp2
        # when train reaches at its final station, its direction will change
        if self.station_num == total_station and self.direction == 0:
            self.direction = 1
        elif self.station_num == 1 and self.direction == 1:
            self.direction = 0
        if self.direction == 0:
            # using temp so that when train reach its final station, then only direction will change and the station
            # number will remain same
            if temp == 1 and self.station_num == 1:
                temp = 0
            else:
                self.station_num += 1  # if not final station station number will increment
        else:
            # this code block is for train tracing back its path to reach the starting station, so this time, station
            # number will decrement
            if temp == 0 and self.station_num == total_station:
                temp = 1
            else:
                self.station_num -= 1
        # after every call to this method, train number will change
        if train_number == 1:
            temp1 = temp
            train_number = 2
        else:
            temp2 = temp
            train_number = 1

    def next_station(self, last_station):
        """This method will tell the station number towards which the train will be moving next"""
        # if train at its final destination, then train will not be going anywhere but only change its direction
        if (last_station == 1 and self.direction == 1) or (last_station == station_total and self.direction == 0):
            next_station = last_station
        elif self.direction == 0 and last_station < station_total:
            next_station = last_station + 1
        else:
            next_station = last_station - 1
        return next_station

    def passengers(self):
        """this method will tell # of arriving passengers(generated randomly) and the passengers that got on board and
        those who are left behind"""

        # accessing the last_time dictionary to get the # of passengers that were left behind by the last train
        waiting_passengers = last_time.get(str(self.direction) + '-' + str(self.station_num), 0)
        new_passengers = 0
        pass_getting_off = 0
        pass_getting_on = 0
        metro_capacity = 250

        # if arriving passengers are more than the available seats, then some of them will be left behind to board
        # next train
        if (self.station_num == 1 and self.direction == 0) or (
                self.station_num == station_total and self.direction == 1):
            # if train at its starting station there will be no passengers aboard, so, no passenger will be leaving the
            # train but only new ones will be arriving
            new_passengers = random.randrange(0, 300)
            if new_passengers <= metro_capacity:
                waiting_passengers = 0
                pass_getting_on = new_passengers
                self.pass_total = new_passengers
            else:
                waiting_passengers = new_passengers - metro_capacity
                pass_getting_on = metro_capacity
                self.pass_total = pass_getting_on
        elif (self.station_num == station_total and self.direction == 0) or (
                self.station_num == 1 and self.direction == 1):
            # when train is at its final station all the passengers will get off.
            pass_getting_off = self.pass_total
            self.pass_total = 0
            waiting_passengers = 0
        else:
            # for any other station than first and last one, this statement will be executed
            new_passengers = random.randrange(0, 300)
            pass_getting_off = random.randrange(0, self.pass_total)
            self.pass_total -= pass_getting_off
            available_seats = metro_capacity - self.pass_total
            if new_passengers + waiting_passengers <= available_seats:
                waiting_passengers = 0
                pass_getting_on = new_passengers + waiting_passengers
                self.pass_total += pass_getting_on
            else:
                waiting_passengers = (new_passengers + waiting_passengers) - available_seats
                pass_getting_on = available_seats
                self.pass_total = metro_capacity
        return waiting_passengers, new_passengers, pass_getting_on, pass_getting_off

    def display(self, s_total, user_direction):
        """this method will print the details about the metro"""
        if user_direction == "ns":
            directions = ["north", "south"]
        elif user_direction == "ne":
            directions = ["north", " east"]
        elif user_direction == "nw":
            directions = ["north", " west"]
        elif user_direction == "se":
            directions = ["south", " east"]
        elif user_direction == "sw":
            directions = ["south", " west"]
        else:
            directions = [" east", " west"]

        print("|##########################################################################|")
        # calling change_station method to change station number and the direction of train when necessary
        self.change_station(s_total)
        # calling passengers method to know the # of passengers on board, waiting and getting off.
        waiting_passengers, new_passengers, pass_getting_on, pass_getting_off = self.passengers()
        print("|                                                                          |")
        print(
            f"| Metro {str(self.metro_id).zfill(3)} at Station number {str(self.station_num).zfill(2)}                "
            f"                           |"
            f"\n| (New passengers waiting {str(new_passengers).zfill(3)})                                             |"
            f"\n| (Passengers left from last time "
            f"{str(last_time.get(str(self.direction) + '-' + str(self.station_num), 0)).zfill(3)})                    "
            f"                 |")
        print("|--------------------------------------------------------------------------|")
        if train_number == 2:
            # we will not be keeping record of the passengers that are left behind by the second train and assigning
            # its value to zero
            last_time[str(self.direction) + "-" + str(self.station_num)] = 0
        else:
            last_time[str(self.direction) + "-" + str(self.station_num)] = waiting_passengers

        print(
            f"| Metro {str(self.metro_id).zfill(3)} leaving station no. {str(self.station_num).zfill(2)} "
            f"{directions[self.direction]} bound with {str(self.pass_total).zfill(3)} passenger(s).      |"
            f"\n|\t   Passenger(s) got off: {str(pass_getting_off).zfill(3)}                                          "
            f" |"
            f"\n|\t   Passenger(s) new passengers waiting to board: {str(new_passengers).zfill(3)}                   |"
            f"\n|\t   Passenger(s) got on: {str(pass_getting_on).zfill(3)}                                            |"
            f"\n|\t   Passenger(s) left behind waiting for next train: {str(waiting_passengers).zfill(3)}             "
            f"   |")
        print("|                                                                          |")
        print("|##########################################################################|")


# calling welcome function
station_total, station_name, required_direction = welcome()

# creating class objects and constructor is automatically called when object is created
train1 = A1Metro()
train2 = A1Metro()

print(f"\n ==> You will be following two metros with metro id {str(train1.metro_id)} and {str(train2.metro_id)}."
      f"\n ==> Both metros will be moving in same direction and metro {str(train2.metro_id)} will be following metro "
      f"{str(train1.metro_id)}."
      f"\n ==> When you quit, you will see the comparison table for both trains.\n")

want_to_continue = True  # want_to_continue is being used to create a loop until its value is 'false'
start_second = False
temp1 = 0  # temp 1 and temp 2 are temporary variables that are being used to help change the direction of metros
temp2 = 0
train_number = 1  # train_number tell which train is being looked at
last_time = {}  # this will store the passengers left from last train
count_train1 = 0  # count_train will be used to store the number of stations the metro has passed
count_train2 = 0
while want_to_continue:
    if not start_second:
        # this block of code will run only once when train 1 is at station 1 and train 2 has not been started yet
        train1.display(station_total, required_direction.lower())
        print("\nName of station number {:02d} ==> {}".format(train1.station_num, station_name[train1.station_num]))
        count_train1 += 1
        start_second = True  # once the train 1 leave station 1, second train will start
    else:
        # making call to display method using objects that we created
        train1.display(station_total, required_direction.lower())
        count_train1 += 1
        train2.display(station_total, required_direction.lower())
        count_train2 += 1
        print("\nName of station number {:02d} ==> {}".format(train1.station_num, station_name[train1.station_num]))
        print("Name of station number {:02d} ==> {}".format(train2.station_num, station_name[train2.station_num]))

    print("\n-------------------------------------------------------------------------------")
    choice = input(
        f'Do you want to continue following Metro train {str(train1.metro_id)} and {str(train2.metro_id)}?'
        f'\nType "n" or "N" for no, anything else for yes: ')
    print()
    if choice.lower() == "n":
        want_to_continue = False
else:
    next_stn1 = train1.next_station(train1.get_station_num())  # to get the next station number
    next_stn2 = train2.next_station(train2.get_station_num())
    # compare will print a table
    compare(train1.get_metro_id(), train2.get_metro_id(), train1.get_station_num(), train2.get_station_num(), next_stn1,
            next_stn2, train1.pass_total, train2.pass_total, train1.get_direction(required_direction),
            train2.get_direction(required_direction), count_train1, count_train2)
    print(f"\n\n*********************************************\n"
          f"\n----[Thank you for using Metro Manager]----"
          f"\nBe sure to look out for future enhancements!"
          f"\n\n\t\t\t\t＼( ･_･)")

exit()  # terminate the program

# last updated on April 15,2021
