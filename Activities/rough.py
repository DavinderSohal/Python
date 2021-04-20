# -----------------------------------------------------------------------
# Assignment 1 | A1 Metro Control
# Written by:
# Short Description of your project/code and how you designed it.
# -----------------------------------------------------------------------
import random
from random import randint


class train:

    def __init__(self):
        self.metro_Id = random.randint(1, 1000)
        self.stationNumber = 0
        self.direction = 1
        self.pass_total = 0
        self.total_passengers = 0
        self.passengers_go_in = 0
        self.passengers_left = 0

    def metroId(self, metroID):
        self.metro_Id = metroID
        self.stationNumber = 0
        self.direction = 0
        self.pass_total = 0

    def get_metroId(self):
        return self.metro_Id

    def get_stationNumber(self):
        return self.stationNumber

    def get_direction(self):
        return self.direction

    def get_totalPass(self):
        return self.pass_total

    def set_metroId(self, metroId):
        self.metro_Id = metroId

    def set_stationNumber(self, stationNumber):
        self.stationNumber = stationNumber

    def set_direction(self, direction):
        self.direction = direction

    def set_totalPass(self, totalPass):
        self.pass_total = totalPass

    def nextStation(self, lastStation):
        if (self.stationNumber == station_number):
            self.direction = -1
        else:
            self.direction = 1
        return self.direction

    def passenger(self):

        print("Metro ID :", self.metro_Id, "Station :", self.stationNumber)
        print("Passenger(s) got off :", self.psnleaving)
        print("Passenger(s) new passengers waiting to board :", self.psnwaiting)
        print("Passenger(s) got on :", self.passengers_go_in)
        print("Passenger(s) left behind waiting for next train :", self.passengers_left)


train1 = train()
train1.set_stationNumber(1)
print("Welcome to Metro tracker")
print("-----------------------------------------")
stations_number = int(input("Enter number of metro stations (minimum 3): "))
while stations_number < 3:
    print("Wrong input!Please enter again.")
    stations_number = int(input("Enter number of metro stations (minimum 3): "))


print("This Metro line has", stations_number, "stations.")

cont = True
while cont:
    station_number = train1.get_stationNumber()
    direction = train1.get_direction()
    print("------------------------------------------------------------------")
    train1.psnwaiting = randint(0, 300)
    train1.psnleaving = randint(0, train1.pass_total)

    train1.pass_total = train1.get_totalPass() - train1.passengers_go_in
    train1.passengers_go_in = min(250 - train1.get_totalPass(), train1.psnwaiting)
    train1.set_totalPass(train1.get_totalPass() + train1.passengers_go_in)
    train1.passengers_left = train1.psnwaiting - train1.passengers_go_in
    train1.passenger()
    print("Do you want to continue following Metro train ", train1.metro_Id, "?")
    user_input = input("Type 'y' or 'Y' for yes, anything else for no : ")

    if user_input.lower() != "y":
        cont = False

    if (station_number == 1 and direction == 1) or (station_number == stations_number and direction == -1):
        train1.set_stationNumber(station_number + direction)
    elif (station_number == stations_number and direction == 1) or (station_number == 1 and direction == -1):
        train1.set_direction(-direction)
    else:
        train1.set_stationNumber(station_number + direction)

else:
    print("------------------------------------------------------------------")
    print("Thank you for using metro station manager")
    exit()
