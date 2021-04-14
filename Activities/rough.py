# from random import randint
#
#
# class train:
#     """
#     Class train to represent a train.
#
#     Have following attributes:
#         i. metroID
#         ii. stationNum which keeps track of the station that the train is at.
#         iii. direction which keeps track of the direction the train is travelling in.
#         iv. passTotal which keeps track of the number of passengers currently on the train.
#     """
#
#     # Constructor of class train.
#     def _init_(self, metro_id = randint(1, 1000)):
#         self.metroID = metro_id
#         self.stationNum = 0
#         self.direction = 1
#         self.passTotal = 0
#
#     # Accessor method of metroID attribute.
#     def getMetroID(self):
#         return self.metroID
#
#     # Accessor method of stationNum attribute.
#     def getStationNum(self):
#         return self.stationNum
#
#     # Accessor method of direction attribute.
#     def getDirection(self):
#         return self.direction
#
#     # Accessor method of passTotal attribute.
#     def getPassTotal(self):
#         return self.passTotal
#
#     # Mutator method of metroID attribute.
#     def setMetroID(self, metro_id):
#         self.metroID = metro_id
#
#     # Mutator method of stationNum attribute.
#     def setStationNum(self, station_num):
#         self.stationNum = station_num
#
#     # Mutator method of direction attribute.
#     def setDirection(self, direction):
#         self.direction = direction
#
#     # Mutator method of passTotal attribute.
#     def setPassTotal(self, pass_total):
#         self.passTotal = pass_total
#
#     # Method to determine the next station the train is to go to.
#     def nextStation(self, lastStation):
#         if (self.stationNum + self.direction > lastStation) or (self.stationNum + self.direction < 1):
#             self.direction = -self.direction
#         return self.stationNum + self.direction
#
#     # String representation method
#     def __str__(self):
#         return "Metro {} leaving station {} {} with {} passenger(s)".format(
#             self.metroID,
#             self.stationNum,
#             "east bound" if self.direction == 1 else "west bound",
#             self.passTotal
#             )
#
#
# # Program Driver
# if __name__ == '__main__':
#     print("Welcome to Metro Manager - Enjoy your metro experience")
#     print("-" * 70)
#
#     while True:
#         numStations = int(input("Enter number of metro stations (minimum 3): "))
#         if numStations >= 3:
#             break
#
#     print("This Metro has 3 stations.\n")
#
#     # Create Train object.
#     t = train()
#     t.setStationNum(1)
#
#     passengersLeft = {i: [0, 0, 0] for i in range(0, numStations + 1)}
#
#     while True:
#         newPassengers = randint(0, 300)
#         snum = t.getStationNum()
#         direction = t.getDirection()
#
#         print("-" * 70)
#
#         # If the metro train is at the 1st station in any given direction,
#         # there will only be people waiting to get on as the train is empty.
#         if ((snum == 1 and direction == 1) or (snum == numStations and direction == -1)):
#             print("Only in")
#             print(f"(New Passengers waiting {newPassengers})")
#             print(f"(Passengers left from last time {passengersLeft[snum][1 + direction]})")
#
#         # If the metro train is at the last station, all passengers must get off
#         # and no one can get on until the train turns around.
#         elif ((snum == numStations and direction == 1) or (snum == 1 and direction == -1)):
#             print("All out")
#             newPassengers = 0
#
#         else:
#             print("In the middle")
#             print(f"(Passengers left from last time {passengersLeft[snum][1 + direction]})")
#
#         print("-" * 70)
#
#         toBoard = newPassengers + passengersLeft[snum][1 + direction]
#
#         gotOff = randint(0, t.getPassTotal())
#
#         if ((snum == numStations and direction == 1) or (snum == 1 and direction == -1)):
#             gotOff = t.getPassTotal()
#
#         t.setPassTotal(t.getPassTotal() - gotOff)
#
#         # If the number of places available on the train,
#         # after people leave is less than the number of people
#         # waiting to get on, some people will be left waiting
#         # on the platform for the next train.
#         gotOn = min(250 - t.getPassTotal(), toBoard)
#         t.setPassTotal(t.getPassTotal() + gotOn)
#         passengersLeft[snum][1 + direction] = toBoard - gotOn
#
#         # Display Details
#         print(t)
#         print("\tPassenger(s) got off:", gotOff)
#         print("\tPassenger(s) new passengers waiting to board:", toBoard)
#         print("\tPassenger(s) got on:", gotOn)
#         print("\tPassenger(s) left behind waiting for next train:", passengersLeft[snum][1 + direction])
#         print(f"\nDo you want to continue following Metro train {t.getMetroID()}?")
#
#         # Ask the user if they would like to continue following the metro.
#         ch = input("Type \"y\" or \"Y\" for yes, anything else for no: ")
#
#         if ((snum == 1 and direction == 1) or (snum == numStations and direction == -1)):
#             t.setStationNum(snum + direction)
#         elif ((snum == numStations and direction == 1) or (snum == 1 and direction == -1)):
#             t.setDirection(-direction)
#         else:
#             t.setStationNum(snum + direction)
#
#         if ch.lower() != "y":
#             break


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


def compare(metro_id1, metro_id2, current_station1, current_station2):
    print("---------------------------------------------------------------")
    print(f"|                   |      metro {str(metro_id1)}      |      metro {metro_id2}      |")
    print( "|-------------------|---------------------|---------------------|")
    print(f"| Current Station   |  Station No. {current_station1}  |  Station No. {current_station2}  |")
    print( "|-------------------|---------------------|---------------------|")
    print(f"| Current Station   |  Station No. {current_station1}  |  Station No. {current_station2}  |")


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

    def next_station(self, last_station):
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
        # next_station = self.next_station(self.station_num)
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
    compare(train1.metro_id,train2.metro_id,train1.station_num,train2.station_num)
    print(f"\n\n*********************************************\n"
          f"\n----[Thank you for using Metro Manager]----"
          f"\nBe sure to look out for future enhancements!"
          f"\n\n\t\t\t\t＼( ･_･)")

exit()
