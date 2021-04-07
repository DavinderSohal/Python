# # x = 'global'
# #
# #
# # def func():
# #     x = x * 2
# #     print(x)
# #
# #
# # func()
#
# import random
#
#
# class Metro:
#     def station(self):
#         while True:
#             station_num = int(input("Enter the number of station: "))
#             if station_num >= 3:
#                 for i in range(station_num):
#                     stationname = input("Enter the name of the station: ")
#                     # station_num = station_num - 1
#                     # print(stationname)
#                 break
#             else:
#                 pass
#                 # print(" ")
#         return station_num
#
#     def metro_id(self):
#         metroid = random.randrange(1, 1000)
#         return metroid
#
#     def moving_train(self, id, stationum):
#         first_station = 0
#         leaving_passengers = 0
#         arriving_passengers = 0
#         print(">>>>>======" + str(id))
#         print(">>>>>" + str(stationum))
#         print("rrrrrr " + str(range(stationum)))
#         for i in range(stationum):
#             print("IIIIIIIIIIIIIIIIIII " + str(i))
#             if i == 0:
#                 arriving_passengers = random.randrange(1, 300)
#                 if arriving_passengers > 250:
#                     waiting_passengers = arriving_passengers - 250
#                     print("Waiting: " + str(waiting_passengers))
#                 else:
#                     print("The passengers are " + str(arriving_passengers))
#
#
# print("WELCOME TO THE METRO MANAGER- ENJOY YOUR METRO EXPERIENCE")
# print("-----------------------------------------------------------")
# train = Metro()
# stationum = train.station()
# print(stationum)
# id = train.metro_id()
# print(id)
# train.moving_train(id, stationum)


import random


class Metro:
    def Station(self):
        while True:
            Station_num = int(input("Enter the number of station: "))
            if Station_num >= 3:
                for i in range(Station_num):
                    stationname = input("Enter the name of the station: ")
                    # Station_num = Station_num - 1
                    print(stationname)
                break
            else:
                print(" ")
        return Station_num

    def metro_id(self):
        metroid = random.randrange(1, 1000)
        return metroid

    def Movingtrain(self, id, stationum):
        for i in range(int(stationum)):
            waiting_passengers = 0
            if i == 0:
                arriving_passengers = random.randrange(1, 300)
                if arriving_passengers > 250:
                    waiting_passengers = arriving_passengers - 250
                    print("The waiting passengers are " + str(waiting_passengers) + "arriving passengers are " + str(
                        arriving_passengers))
                else:
                    print("The passengers are " + str(arriving_passengers))
            elif i < stationum:
                arriving_passengers = random.randrange(1, 300)
                leaving_passengers = random.randrange(1, arriving_passengers)
                if (arriving_passengers + waiting_passengers) > 250:
                    waiting_passengers = arriving_passengers - 250
                    print("The arriving passenger are " + str(arriving_passengers) + "waiting passenger are " + str(
                        waiting_passengers))
                    print("The leaving passengers are " + str(leaving_passengers))
                else:
                    print("The arriving passenger are " + str(arriving_passengers) + "leaving passenger are " + str(
                        leaving_passengers))
            else:
                leaving_passengers = random.randrange(1, 250)
                arriving_passengers = 0
                print(
                    "The arriving passengers are " + str(arriving_passengers) + "and the leaving passengers are " + str(
                        leaving_passengers))


print("WELCOME TO THE METRO MANAGER- ENJOY YOUR METRO EXPERIENCE")
print("-----------------------------------------------------------")
train = Metro()
stationum = train.Station()
print(stationum)
id = train.metro_id()
print(id)
train.Movingtrain(id, stationum)
