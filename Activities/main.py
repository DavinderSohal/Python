import random  # module used to select the random train no., passengers count....


class TrainTracker:
    def __init__(self):
        self.m_id = 0
        self.station_num = 0
        self.direction = 0
        self.pass_total = 0

    # Accessor method of metroID attribute.
    def get_metro_id(self):
        return self.m_id

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
        self.m_id = metro_id

    # Mutator method of stationNum attribute.
    def set_station_num(self, station_num):
        self.station_num = station_num

    # Mutator method of direction attribute.
    def set_direction(self, direction):
        self.direction = direction

    # Mutator method of passTotal attribute.
    def set_pass_total(self, pass_total):
        self.pass_total = pass_total

    def display(self):
        # welcome message
        print()
        print("------------------------------------------------------")
        print("Welcome to Metro Manager - Enjoy your Metro experience")
        print("------------------------------------------------------")

        while True:
            station = int(input("Enter the number of Metro stations ( minimum 3 ) : "))
            if station <= 2:
                # will iterate until station variable ' >= 3 '
                print()
                print("----------------------------------------")
                print("you have to select at least 3 stations...")
                print("----------------------------------------")
                print()
                continue

            else:
                metro_id = random.randint(1, 1000)  # will select randomly any number between 1 to 1000 for Metro id
                while True:
                    print("This Metro line has", station, "stations")  # will print the total no. of stations
                    print("---------------------------------")
                    direction_forward = "east"  # shows the direction of the train
                    # departing from 1st station 
                    print("Only in")
                    pass_total = random.randint(1, 250)  # random count that no. of passengers present inside the train
                    print("New passengers waiting", pass_total)
                    print("Passengers left from last time 0")
                    print("---------------------------------")
                    print("Metro", metro_id, "(new train) leaving station 1", direction_forward, "bond with",
                          pass_total,
                          "passenger(s)")
                    print("\t Passenger(s) got off : 0")  # no one will get off the train at 1st station itself
                    print("\t Passenger(s) new passengers waiting to board", pass_total)
                    print("\t Passenger(s) got on :", pass_total)
                    print("\t Passenger(s) left behind waiting for next train : 0")
                    print("---------------------------------------------------------------")
                    print("Type 'y' or 'Y' for yes, anything else for no")
                    conform = input("Do you want to continue following Metro train : ")
                    print("---------------------------------------------------------------")
                    if conform == 'y' or conform == 'Y':
                        # will iterate for the in between stations ( except first and last station )
                        for f in range(2, station):
                            print("In the middle")
                            print("Passengers left from last time 0")
                            print("---------------------------------")
                            got_off = random.randint(1, pass_total)  # random count for those who got off from the train
                            if pass_total < got_off:  # decorator
                                got_off, pass_total = pass_total, got_off  # swap the numbers to avoid the negative
                                # values
                            balance = pass_total - got_off  # subtracting passengers count and got off count
                            cap_pass = 250  # total capacity of passengers count
                            if balance < cap_pass:  # decorator
                                balance, cap_pass = cap_pass, balance  # swap the numbers to avoid the negative values
                            capacity = balance - cap_pass  # present capacity of the train
                            got_on = random.randint(1, capacity)  # random count for getting on to the train
                            a = got_on + balance  # adding rest peoples in the train and new peoples
                            new_old_pass = a - capacity  # passengers count (new + old passengers)
                            print("Metro", metro_id, "leaving station", f, direction_forward, "bond with", new_old_pass,
                                  "passenger(s)")
                            print("\t Passenger(s) got off :", got_off)
                            print("\t Passenger(s) new passengers waiting to board : ", got_on)
                            print("\t Passenger(s) got on : ", got_on)
                            print("\t Passenger(s) left behind waiting for next train : 0")
                            print("---------------------------------------------------------------")
                            print("Type 'y' or 'Y' for yes, anything else for no")
                            conform = input("Do you want to continue following Metro train : ")
                            print("---------------------------------------------------------------")
                            if conform == 'y' or conform == 'Y':
                                pass  # will track reversibly to the departed station
                            else:
                                # closing message
                                print(
                                    "Thank you for using Metro manager 3.0 \nBe sure to look out for future "
                                    "enhancements")
                                exit()
                    else:
                        # closing message
                        print("Thank you for using Metro manager 3.0 \nBe sure to look out for future enhancements")
                        exit()

                    # last station 
                    print("All out")
                    print("-------")
                    print("Metro", metro_id, "leaving station", station, direction_forward, "bond with 0 passenger(s)")
                    print("\t Passenger(s) got off :", new_old_pass)  # all should get off from the train
                    print("\t Passenger(s) new passengers waiting to board : 0")
                    print("\t Passenger(s) got on : 0")  # no one will get on at the last station
                    print("\t Passenger(s) left behind waiting for next train : 0")
                    print(
                        "---------------------------------------------------------"
                        "-------------------------------------------------------------")
                    print(
                        "Type 'y' or 'Y' for continue with the same train, Type 't' or 'T' to go for another train, "
                        "anything else for no")

                    direction_backward = "west"  # shows the direction of the train
                    conform = input("Do you want to continue following Metro train : ")
                    print("---------------------------------------------------------------")
                    if conform == 't' or conform == 'T':
                        # New metro
                        while True:
                            # will iterate until station variable ' >= 3 '
                            station = int(input("Enter the number of Metro stations ( minimum 3 ) : "))
                            if station <= 2:
                                print()
                                print("----------------------------------------")
                                print("you have to select at least 3 stations...")
                                print("----------------------------------------")
                                print()
                                continue
                            else:
                                # will start from new train
                                break
                        metro_id = random.randint(1, 1000)  # new metro id
                        continue
                    elif conform == 'y' or conform == 'Y':  # opposite side movement
                        # 1st station
                        print("---------------------------------")
                        print("Only in")
                        pass_total = random.randint(1,
                                                    250)  # random count that no. of passengers present inside the train
                        print("New passengers waiting", pass_total)
                        print("Passengers left from last time 0")
                        print("---------------------------------")
                        print("Metro", metro_id, "leaving station", station, direction_backward, "bond with",
                              pass_total,
                              "passenger(s)")
                        print("\t Passenger(s) got off : 0")  # no one will get off the train at 1st station itself
                        print("\t Passenger(s) new passengers waiting to board", pass_total)
                        print("\t Passenger(s) got on :", pass_total)
                        print("\t Passenger(s) left behind waiting for next train : 0")
                        print("Type 'y' or 'Y' for yes, anything else for no")
                        conform = input("Do you want to continue following Metro train : ")
                        print("---------------------------------------------------------------")
                        if conform == 'y' or conform == 'Y':
                            for r in range(station, 2,
                                           -1):  # will iterate for the in between stations ( except first and last
                                # station )
                                print("In the middle")
                                print("Passengers left from last time 0")
                                print("---------------------------------")
                                got_off = random.randint(1,
                                                         pass_total)  # random count for those who got off from the
                                # train
                                if pass_total < got_off:  # decorator
                                    got_off, pass_total = pass_total, got_off  # swap the numbers to avoid the negative
                                    # values
                                balance = pass_total - got_off  # subtracting passengers count and got off count
                                cap_pass = 250  # total capacity of passengers count
                                if balance < cap_pass:  # decorator
                                    balance, cap_pass = cap_pass, balance  # swap the numbers to avoid the negative
                                    # values
                                capacity = balance - cap_pass  # present capacity of the train
                                got_on = random.randint(1, capacity)  # random count for getting on to the train
                                a = got_on + balance  # adding rest peoples in the train and new peoples
                                new_old_pass = a - capacity  # passengers count (new + old passengers)
                                print("Metro", metro_id, "leaving station", r - 1, direction_backward, "bond with",
                                      new_old_pass, "passenger(s)")
                                print("\t Passenger(s) got off :", got_off)
                                print("\t Passenger(s) new passengers waiting to board : ", got_on)
                                print("\t Passenger(s) got on : ", got_on)
                                print("\t Passenger(s) left behind waiting for next train : 0")
                                print("---------------------------------------------------------------")
                                print("Type 'y' or 'Y' for yes, anything else for no")
                                conform = input("Do you want to continue following Metro train : ")
                                print("---------------------------------------------------------------")
                                if conform == 'y' or conform == 'Y':
                                    # will track reversibly to the departed station
                                    pass
                                else:
                                    # closing message
                                    print(
                                        "Thank you for using Metro manager 3.0 \nBe sure to look out for future "
                                        "enhancements")
                                    exit()
                        else:
                            # closing message
                            print("Thank you for using Metro manager 3.0 \nBe sure to look out for future enhancements")
                            exit()

                        # last station 
                        print("All out")
                        print("-------")
                        print("Metro", metro_id, "leaving station 1", direction_backward, "bond with 0 passenger(s)")
                        print("\t Passenger(s) got off :", new_old_pass)  # all should get off from the train
                        print("\t Passenger(s) new passengers waiting to board : 0")
                        print("\t Passenger(s) got on : 0")  # no one will get on at the last station
                        print("\t Passenger(s) left behind waiting for next train : 0")
                        print(
                            "---------------------------------------------------------------------------------------"
                            "-------------------------------")
                        print(
                            "Type 'y' or 'Y' for continue with the same train, Type 't' or 'T' to go for another "
                            "train, anything else for no")
                        conform = input("Do you want to continue following Metro train : ")
                        print("---------------------------------------------------------------")
                        if conform == 't' or conform == 'T':
                            # New metro
                            while True:
                                # will iterate until station variable ' >= 3 '
                                station = int(input("Enter the number of Metro stations ( minimum 3 ) : "))
                                if station <= 2:
                                    print()
                                    print("----------------------------------------")
                                    print("you have to select at least 3 stations...")
                                    print("----------------------------------------")
                                    print()
                                    continue
                                else:
                                    # will start from new train
                                    break
                            metro_id = random.randint(1, 1000)  # new metro id
                            continue
                        elif conform == 'y' or conform == 'Y':
                            # will continue with the same metro id
                            pass
                        else:
                            # closing message
                            print("Thank you for using Metro manager 3.0 \nBe sure to look out for future enhancements")
                            exit()

                    else:
                        # closing message
                        print("Thank you for using Metro manager 3.0 \nBe sure to look out for future enhancements")
                        exit()


train = TrainTracker()  # object for class
train.display()
