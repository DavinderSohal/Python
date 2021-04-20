import random


class Train:

    def __init__(self, metroId = random.randint(1, 1000)):
        self.metroId = metroId

        self.stationNum = 1

        self.direction = 'North'

        self.passTotal = 0

    def set_metroId(self, metroId):
        self.metroId = metroId

    def get_metroId(self):
        return self.metroId

    def set_stationNum(self, stationNum):
        self.stationNum = stationNum

    def get_stationNum(self):
        return self.stationNum

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_passTotal(self, passTotal):
        self.passTotal = passTotal

    def get_passTotal(self):
        return self.passTotal

    def nextStation(self, lastStation):
        self.stationNum = lastStation + 1


print("Welcome to Metro Manager - Enjoy your metro experience")

num_of_stations = int(input("Enter number of metro stations (minimum 3): "))

print("This Metro line has {} stations.".format(num_of_stations))

train = Train()

input_from_user = "y"
while input_from_user == 'y':
    if train.get_stationNum() == 1:

        if train.get_direction() == 'North':
            total_passengers_onboarding = random.randint(1, 100)
            total_passengers_disembarking = 0
            total_passengers_in_platform = random.randint(total_passengers_onboarding, 300)

            train.set_passTotal(total_passengers_onboarding)
            print("Metro {} (new Train) leaving station {} {} bound with {} passenger(s).".format(train.get_metroId(),
                                                                                                  train.get_stationNum(),
                                                                                                  train.get_direction(),
                                                                                                  train.get_passTotal()))
            print("Passenger(s) got off:{}".format(total_passengers_disembarking))
            print("Passenger(s) new passengers waiting to board: {}".format(total_passengers_in_platform))
            print("Passenger(s) got on: {}".format(total_passengers_onboarding))
            print("Passenger(s) left behind waiting for next train: {}".format(
                total_passengers_in_platform - total_passengers_onboarding))
            train.set_stationNum(train.get_stationNum() + 1)

        else:
            total_passengers_onboarding = 0
            total_passengers_disembarking = train.get_passTotal()
            total_passengers_in_platform = 0

            train.set_passTotal(total_passengers_onboarding)

            print("Metro {} (new Train) leaving station {} {} bound with {} passenger(s).".format(train.get_metroId(),
                                                                                                  train.get_stationNum(),
                                                                                                  train.get_direction(),
                                                                                                  train.get_passTotal()))
            print("Passenger(s) got off:{}".format(total_passengers_disembarking))
            print("Passenger(s) new passengers waiting to board: {}".format(total_passengers_in_platform))
            print("Passenger(s) got on: {}".format(total_passengers_onboarding))
            print("Passenger(s) left behind waiting for next train: {}".format(
                total_passengers_in_platform - total_passengers_onboarding))

            train.set_direction("North")


    elif train.get_stationNum() == num_of_stations:

        if train.get_direction() == 'North':
            total_passengers_onboarding = 0
            total_passengers_disembarking = train.get_passTotal()
            total_passengers_in_platform = 0

            train.set_passTotal(total_passengers_onboarding)
            print("Metro {} (new Train) leaving station {} {} bound with {} passenger(s).".format(train.get_metroId(),
                                                                                                  train.get_stationNum(),
                                                                                                  train.get_direction(),
                                                                                                  train.get_passTotal()))
            print("Passenger(s) got off:{}".format(total_passengers_disembarking))
            print("Passenger(s) new passengers waiting to board: {}".format(total_passengers_in_platform))
            print("Passenger(s) got on: {}".format(total_passengers_onboarding))
            print("Passenger(s) left behind waiting for next train: {}".format(
                total_passengers_in_platform - total_passengers_onboarding))
            train.set_direction("South")

        else:

            total_passengers_onboarding = random.randint(1, 100)
            total_passengers_disembarking = 0
            total_passengers_in_platform = random.randint(total_passengers_onboarding, 300)

            train.set_passTotal(total_passengers_onboarding)
            print("Metro {} (new Train) leaving station {} {} bound with {} passenger(s).".format(train.get_metroId(),
                                                                                                  train.get_stationNum(),
                                                                                                  train.get_direction(),
                                                                                                  train.get_passTotal()))
            print("Passenger(s) got off:{}".format(total_passengers_disembarking))
            print("Passenger(s) new passengers waiting to board: {}".format(total_passengers_in_platform))
            print("Passenger(s) got on: {}".format(total_passengers_onboarding))
            print("Passenger(s) left behind waiting for next train: {}".format(
                total_passengers_in_platform - total_passengers_onboarding))
            train.set_stationNum(train.get_stationNum() - 1)

    else:

        total_passengers_onboarding = random.randint(1, 100)
        total_passengers_disembarking = random.randint(1, train.get_passTotal())
        total_passengers_in_platform = random.randint(total_passengers_onboarding, 300)

        train.set_passTotal(train.get_passTotal() + total_passengers_onboarding - total_passengers_disembarking)

        print("Metro {} (new Train) leaving station {} {} bound with {} passenger(s).".format(train.get_metroId(),
                                                                                              train.get_stationNum(),
                                                                                              train.get_direction(),
                                                                                              train.get_passTotal()))
        print("Passenger(s) got off:{}".format(total_passengers_disembarking))
        print("Passenger(s) new passengers waiting to board: {}".format(total_passengers_in_platform))
        print("Passenger(s) got on: {}".format(total_passengers_onboarding))
        print("Passenger(s) left behind waiting for next train: {}".format(
            total_passengers_in_platform - total_passengers_onboarding))
        if train.get_direction() == 'North':
            train.set_stationNum(train.get_stationNum() + 1)
        else:
            train.set_stationNum(train.get_stationNum() - 1)

    input_from_user = input('''Do you want to continue following Metro train {}?
Type "y" or "Y" for yes, anything else for no: '''.format(train.get_metroId()))

print('''Thank you for using Metro Manager 3.0
Be sure to look out for future enhancements!''')
