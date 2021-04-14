# Assignment 1 Student Id : 2092430 Student name: Simranjit kaur This Assignment is about creating a metro manager
# where a person wants to keep the record of passengers, directions and station number.I designed this program
# with the help of loop, constructors, functions.
# The idea which makes it uniques is that i created two trains


import random


class Metro:

    def __init__(self):
        self.m_id = 0
        self.station_num = 0
        self.direction = 0
        self.pass_total = 0

    # Accessor method of metroID attribute.
    def get_metro_id(self):
        return self.metro_id

    # Accessor method of stationNum attribute.
    def get_station_num(self):
        return self.station_num

    # Accessor method of direction attribute.
    def get_direction(self):
        return self.direction

    # Accessor method of passTotal attribute.
    def get_pass_total(self):
        return self.pass_total

    # Mutator method of metroID attribute.
    def set_metro_id(self, metro_id):
        self.metro_id = metro_id

    # Mutator method of stationNum attribute.
    def set_station_num(self, station_num):
        self.station_num = station_num

    # Mutator method of direction attribute.
    def set_direction(self, direction):
        self.direction = direction

    # Mutator method of passTotal attribute.
    def set_pass_total(self, pass_total):
        self.pass_total = pass_total

    def metro_id(self):
        metroid = random.randrange(1, 1000)
        pass_total = 0
        return metroid, pass_total

    def color1(self, metroid):
        if metroid >= 1 and metroid <= 300:
            color = "blue"
            return color
        elif metroid >= 301 and metroid <= 600:
            color = "yellow"
            return color
        else:
            color = "Green"
            return color

    def Metro_direction(self):
        print("for east to west : 1" + "\n" + "from north to south : 2")
        while True:
            dir = int(input("Enter the direction : "))
            if dir > 0 and dir < 3:
                return dir
            else:
                print("")

    def Station(self):
        while True:
            Station_num = int(input("Enter the number of station: "))
            if Station_num >= 3:
                print("This metro has " + str(Station_num) + " stations")
                for i in range(Station_num):
                    station_name = {}
                    station_name[i + 1] = input("Enter the name of the station: ")
                break
            else:
                print(" ")
        return Station_num

    def Movingtrain(self, id, stationum, metro_direc, total, color):
        direction = ["east", "west", "north", "south"]
        i = 1

        while i <= stationum:
            waiting_passengers = 0
            leaving_passengers = 0
            want_to_continue = " "
            while want_to_continue != "quit":

                if i == 1:
                    arriving_passengers = random.randrange(1, 300)
                    if arriving_passengers > 250:
                        waiting_passengers = arriving_passengers - 250
                        arriving_passengers = arriving_passengers - waiting_passengers
                        total = arriving_passengers
                        print("ONLY IN" + "\n" + "Passengers got off  : " + str(leaving_passengers) + "\n" +
                              "Passengers waiting for metro : " + str(arriving_passengers))
                        if metro_direc == 2:
                            print(
                                "Metro " + str(id) + " is going from station no. " + str(i) + " direction  " + str(
                                    direction[int(metro_direc)] + "   bound with  " + str(
                                        total) + "  passengers in " + color + " line"))
                        else:
                            print("Metro is going from station no. " + str(i) + " direction " + str(
                                direction[int(metro_direc - 1)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")

                        print("Passengers got off  " + str(leaving_passengers) + "\nNew Passengers got in " + str(
                            arriving_passengers) + "\nPassengers left behind for next train " + str(waiting_passengers))
                    else:
                        total = arriving_passengers
                        print("ONLY IN")
                        print("Passengers got off  : " + str(leaving_passengers) + "\n" +
                              "Passengers waiting for metro : " + str(arriving_passengers))
                        if metro_direc == 2:
                            print("Metro " + str(id) + "  is going from station no. " + str(i) +
                                  "  direction " + str(direction[int(metro_direc)]) + " bound with "
                                  + str(total) + " passengers in " + color + " line")
                        else:

                            print("Metro " + str(id) + " is going from station no. " + str(i) + " direction " + str(
                                direction[int(metro_direc - 1)] + " bound with " + str(
                                    total) + " passengers in " + color + " line"))
                        print("Passengers got off  : " + str(
                            leaving_passengers) + "\n" + "Passengers waiting for metro : " + str(
                            arriving_passengers))

                elif i < stationum:
                    print("IN MIDDLE")
                    arriving_passengers = random.randrange(1, 300)
                    leaving_passengers = random.randrange(1, arriving_passengers)
                    if (
                            arriving_passengers + waiting_passengers) > 250 or arriving_passengers > 250 or \
                            arriving_passengers - leaving_passengers > 250:
                        waiting_passengers = arriving_passengers - 250
                        arriving_passengers = arriving_passengers - waiting_passengers
                        total = total + arriving_passengers - leaving_passengers
                        if total > 250:
                            waiting_passengers = total - 250
                            total = total - waiting_passengers
                        if metro_direc == 2:
                            print("Metro " + str(id) + "  is going from station no.  " + str(i) + "  direction " + str(
                                direction[int(metro_direc)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")
                        else:
                            print("Metro " + str(id) + " is going from station no. " + str(i) + " direction " + str(
                                direction[int(metro_direc - 1)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")
                        print("Passengers got in " + str(
                            arriving_passengers) + "\nPassengers waiting for another train " + str(
                            waiting_passengers) + "\nPassengers got off " + str(leaving_passengers))
                    else:
                        total = total + arriving_passengers - leaving_passengers
                        if total > 250:
                            waiting_passengers = total - 250
                            total = total - waiting_passengers

                        if metro_direc == 2:
                            print("Metro " + str(id) + "  is going from station no. " + str(i) + " direction " + str(
                                direction[int(metro_direc)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")
                        else:
                            print("Metro " + str(id) + " is going from station no. " + str(i) + " direction " + str(
                                direction[int(metro_direc - 1)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")
                        print("Passengers got in " + str(
                            arriving_passengers) + "\nPassengers waiting for another train " + str(
                            waiting_passengers) + "\nPassengers got off " + str(leaving_passengers))

                else:
                    leaving_passengers = total
                    arriving_passengers = 0
                    print("ALL OUT")
                    if metro_direc == 2:
                        print("Metro " + str(id) + "  is going from station no. " + str(i) + " direction " + str(
                            direction[int(metro_direc)]) + " bound with " + str(
                            total) + " passengers in " + color + " line")
                    else:
                        print("Metro " + str(id) + " is going from station no. " + str(i) + " direction " + str(
                            direction[int(metro_direc - 1)]) + " bound with " + str(
                            total) + " passengers in " + color + " line")
                    print("Passengers got off " + str(
                        leaving_passengers) + "\nPassenger got in " + str(
                        arriving_passengers))
                i = i + 1
                want_to_continue = input("Do you want to continue?\n Enter quit for stop or anything for continue")
                if want_to_continue == "quit":
                    print("Thankyou")
                    exit()
                elif i == stationum + 1:
                    break
                else:
                    print("----------------------------------------------------------------")
                    continue

    def movingtrain2(self, stationum, metro_direc, total, id, color):
        waiting_passengers = 0
        leaving_passengers = 0
        direction = ["east", "west", "north", "south"]
        j = stationum
        # i = 1
        want_to_continue = " "
        while j >= 1:
            while want_to_continue != "quit":

                print("--------------------------------------------------------------------")
                if j == stationum:
                    arriving_passengers = random.randrange(1, 300)
                    if arriving_passengers > 250:
                        waiting_passengers = arriving_passengers - 250
                        arriving_passengers = arriving_passengers - waiting_passengers

                        total: int = arriving_passengers
                        print("ONLY IN" + "\n" + "Passengers got off  : " + str(leaving_passengers) + "\n" +
                              "Passengers waiting for metro : " + str(arriving_passengers))
                        if metro_direc == 1:
                            print("Metro " + str(id) + " is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc)] + " bound with " + str(
                                    total) + " passengers in " + color + " line"))
                        else:
                            print("Metro is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc + 1)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")

                            print("Passengers got off " + str(leaving_passengers) + "\nNew Passengers got in " + str(
                                arriving_passengers) + "\nPassengers left behind for next train " + str(
                                waiting_passengers))

                    else:
                        total = arriving_passengers
                        print("ONLY IN" + "\n" + "Passengers got off  : " + str(leaving_passengers) + "\n" +
                              "Passengers waiting for metro : " + str(arriving_passengers))
                        if metro_direc == 2:
                            print("Metro " + str(id) + " is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc + 1)] + " bound with " + str(
                                    total) + " passengers in  " + color + " line"))
                        else:
                            print("Metro is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")

                        print("Passengers got off " + str(leaving_passengers) + "\nNew Passengers got in " + str(
                            arriving_passengers) + "\nPassengers left behind for next train " + str(
                            waiting_passengers))
                elif j > 1:
                    print("IN MIDDLE")
                    arriving_passengers = random.randrange(1, 300)
                    leaving_passengers = random.randrange(1, arriving_passengers)
                    if (
                            arriving_passengers + waiting_passengers) > 250 or arriving_passengers > 250 or \
                            arriving_passengers - leaving_passengers > 250:
                        waiting_passengers = arriving_passengers - 250
                        arriving_passengers = arriving_passengers - waiting_passengers
                        total = (arriving_passengers - leaving_passengers) + total
                        if total > 250:
                            waiting_passengers = total - 250
                            total = total - waiting_passengers

                        if metro_direc == 2:
                            print("Metro " + str(id) + "  is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc + 1)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")
                        else:
                            print("Metro " + str(id) + " is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc)]) + " bound with " + str(
                                total) + " passengers  in " + color + " line")
                        print("Passengers got in " + str(
                            arriving_passengers) + "\nPassengers waiting for another train " + str(
                            waiting_passengers) + "\nPassengers got off " + str(leaving_passengers))

                    else:
                        total = total + arriving_passengers - leaving_passengers
                        if total > 250:
                            waiting_passengers = total - 250
                            total = total - waiting_passengers
                        if metro_direc == 2:
                            print("Metro " + str(id) + "  is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc + 1)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")
                        else:
                            print("Metro " + str(id) + " is going from station no. " + str(j) + " direction " + str(
                                direction[int(metro_direc)]) + " bound with " + str(
                                total) + " passengers in " + color + " line")
                        print("Passengers got in " + str(
                            arriving_passengers) + "\nPassengers waiting for another train " + str(
                            waiting_passengers) + "\nPassengers got off " + str(leaving_passengers))
                else:
                    leaving_passengers = total
                    arriving_passengers = 0
                    print("All OUT")
                    if metro_direc == 2:
                        print("Metro " + str(id) + "  is going from station no. " + str(j) + " direction " + str(
                            direction[int(metro_direc + 1)]) + " bound with " + str(
                            total) + " passengers in " + color + " line")
                    else:
                        print("Metro " + str(id) + " is going from station no. " + str(j) + " direction " + str(
                            direction[int(metro_direc)]) + " bound with " + str(
                            total) + " passengers in " + color + " line")
                    print("Passengers got off " + str(
                        leaving_passengers) + "\nPassengers got in " + str(
                        arriving_passengers))
                j = j - 1
                if j == 0:
                    break
                else:
                    want_to_continue = input("Do you want to continue?\n Enter quit for stop or anything for continue")
                    if want_to_continue == "quit":
                        print("Thank you for choosing the metro manager")
                        exit()
                    else:
                        continue


print("WELCOME TO THE METRO MANAGER- ENJOY YOUR METRO EXPERIENCE")
print("-----------------------------------------------------------")
train = Metro()
id, total = train.metro_id()
print("The metro id is " + str(id))
metro_direc = train.Metro_direction()
color = train.color1(id)
stationum = train.Station()
print("---------------------------------------")
train.Movingtrain(id, stationum, metro_direc, total, color)
train.movingtrain2(stationum, metro_direc, total, id, color)
print("\nThank you for having a tour with one of the metro......After this you will enjoy another metro")
print("--------------------------Welcome to New Metro-----------------------")
train2 = Metro()
id1, total = train2.metro_id()
print("The metro id is " + str(id1))
metro_direc = train.Metro_direction()
stationum = train2.Station()
print("---------------------------------------")
train2.Movingtrain(id, stationum, metro_direc, total, color)
train2.movingtrain2(stationum, metro_direc, total, id, color)
