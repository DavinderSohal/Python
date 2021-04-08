# # # x = 'global'
# # #
# # #
# # # def func():
# # #     x = x * 2
# # #     print(x)
# # #
# # #
# # # func()
# #
# # import random
# #
# #
# # class Metro:
# #     def station(self):
# #         while True:
# #             station_num = int(input("Enter the number of station: "))
# #             if station_num >= 3:
# #                 for i in range(station_num):
# #                     stationname = input("Enter the name of the station: ")
# #                     # station_num = station_num - 1
# #                     # print(stationname)
# #                 break
# #             else:
# #                 pass
# #                 # print(" ")
# #         return station_num
# #
# #     def metro_id(self):
# #         metroid = random.randrange(1, 1000)
# #         return metroid
# #
# #     def moving_train(self, id, stationum):
# #         first_station = 0
# #         leaving_passengers = 0
# #         arriving_passengers = 0
# #         print(">>>>>======" + str(id))
# #         print(">>>>>" + str(stationum))
# #         print("rrrrrr " + str(range(stationum)))
# #         for i in range(stationum):
# #             print("IIIIIIIIIIIIIIIIIII " + str(i))
# #             if i == 0:
# #                 arriving_passengers = random.randrange(1, 300)
# #                 if arriving_passengers > 250:
# #                     waiting_passengers = arriving_passengers - 250
# #                     print("Waiting: " + str(waiting_passengers))
# #                 else:
# #                     print("The passengers are " + str(arriving_passengers))
# #
# #
# # print("WELCOME TO THE METRO MANAGER- ENJOY YOUR METRO EXPERIENCE")
# # print("-----------------------------------------------------------")
# # train = Metro()
# # stationum = train.station()
# # print(stationum)
# # id = train.metro_id()
# # print(id)
# # train.moving_train(id, stationum)
#
#
# import random
#
#
# class Metro:
#     def Station(self):
#         while True:
#             Station_num = int(input("Enter the number of station: "))
#             if Station_num >= 3:
#                 for i in range(Station_num):
#                     stationname = input("Enter the name of the station: ")
#                     # Station_num = Station_num - 1
#                     print(stationname)
#                 break
#             else:
#                 print(" ")
#         return Station_num
#
#     def metro_id(self):
#         metroid = random.randrange(1, 1000)
#         return metroid
#
#     def Movingtrain(self, id, stationum):
#         for i in range(int(stationum)):
#             waiting_passengers = 0
#             if i == 0:
#                 arriving_passengers = random.randrange(1, 300)
#                 if arriving_passengers > 250:
#                     waiting_passengers = arriving_passengers - 250
#                     print("The waiting passengers are " + str(waiting_passengers) + "arriving passengers are " + str(
#                         arriving_passengers))
#                 else:
#                     print("The passengers are " + str(arriving_passengers))
#             elif i < stationum:
#                 arriving_passengers = random.randrange(1, 300)
#                 leaving_passengers = random.randrange(1, arriving_passengers)
#                 if (arriving_passengers + waiting_passengers) > 250:
#                     waiting_passengers = arriving_passengers - 250
#                     print("The arriving passenger are " + str(arriving_passengers) + "waiting passenger are " + str(
#                         waiting_passengers))
#                     print("The leaving passengers are " + str(leaving_passengers))
#                 else:
#                     print("The arriving passenger are " + str(arriving_passengers) + "leaving passenger are " + str(
#                         leaving_passengers))
#             else:
#                 leaving_passengers = random.randrange(1, 250)
#                 arriving_passengers = 0
#                 print(
#                     "The arriving passengers are " + str(arriving_passengers) + "and the leaving passengers are " +
#                     str(
#                         leaving_passengers))
#
#
# print("WELCOME TO THE METRO MANAGER- ENJOY YOUR METRO EXPERIENCE")
# print("-----------------------------------------------------------")
# train = Metro()
# stationum = train.Station()
# print(stationum)
# id = train.metro_id()
# print(id)
# train.Movingtrain(id, stationum)


import random


class Metro:
    def metro_id(self):
        metroid = random.randrange(1, 1000)
        pass_total = 0
        return metroid, pass_total

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
                    stationname = {}
                    stationname[i + 1] = input("Enter the name of the station: ")
                    # Station_num = Station_num - 1

                break
            else:
                print(" ")
        return Station_num

    def Movingtrain(self, id, stationum, metro_direc, total):
        direction = ["east", "west", "north", "south"]
        i = 1
        waiting_passengers = 0
        while i <= stationum:
            if i == 1:
                arriving_passengers = random.randrange(1, 300)
                if arriving_passengers > 250:
                    waiting_passengers = arriving_passengers - 250
                    arriving_passengers = arriving_passengers - waiting_passengers
                    # total = arriving_passengers
                    total = 250
                    print("Only in" + "\n" + "New passenger : " + str(
                        arriving_passengers) + "\n" + "Waiting passenger : " + str(waiting_passengers))
                    print("total passenger " + str(total))
                    # print("The waiting passengers are " + str(waiting_passengers) + "arriving passengers are " + str(
                    #     arriving_passengers))
                else:
                    total = arriving_passengers
                    print("The passengers are " + str(total))
                print(str(id) + " Metro is going to station no. " + str(i + 1) + " direction " + str(
                    direction[int(metro_direc)]))

            elif i < stationum:
                arriving_passengers = random.randrange(1, 300)
                # leaving_passengers = random.randrange(1, arriving_passengers)
                leaving_passengers = random.randrange(1, total)
                # if (arriving_passengers + waiting_passengers) > 250:
                if (arriving_passengers + waiting_passengers) > (250 - total + leaving_passengers):
                    # waiting_passengers = arriving_passengers - 250
                    waiting_passengers = arriving_passengers + waiting_passengers - 250 - total
                    arriving_passengers = arriving_passengers - waiting_passengers
                    total = total + arriving_passengers - leaving_passengers
                    print("The arriving passenger are " + str(arriving_passengers) + " waiting passenger are " + str(
                        waiting_passengers))
                    print("total passengers " + str(total))
                    print("The leaving passengers are " + str(leaving_passengers))
                else:
                    # total = total + arriving_passengers - leaving_passengers
                    total = total + arriving_passengers + waiting_passengers - leaving_passengers
                    print("The arriving passenger are " + str(arriving_passengers) + " leaving passenger are " + str(
                        leaving_passengers))
                    print("total passengers : " + str(total))
            else:
                # leaving_passengers = random.randrange(1, 250)
                leaving_passengers = total
                arriving_passengers = 0
                print(
                    "The arriving passengers are " + str(arriving_passengers) + " and the leaving passengers are " + str(
                        leaving_passengers))
                # total = total + leaving_passengers
                total = 0
                print("left passengers : " + str(total))
            i = i + 1
            j = stationum
            while j <= 1:
                # waiting_passengers = 0
                if j == stationum:
                    arriving_passengers = random.randrange(1, 300)
                    if arriving_passengers > 250:
                        waiting_passengers = arriving_passengers - 250
                        arriving_passengers = arriving_passengers - waiting_passengers
                        # total = arriving_passengers
                        total = 250

                        print("Only in" + "\n" + "New passenger : " + str(
                            arriving_passengers) + "\n" + "Waiting passenger : " + str(waiting_passengers))
                        print("total passengers: " + str(total))
                        # print(
                        #     "The waiting passengers are " + str(waiting_passengers) + "arriving passengers are " +
                        #     str(
                        #         arriving_passengers))
                    else:
                        print("Only in" + "\n" + "New passenger : " + str(arriving_passengers))
                        total = arriving_passengers
                        print("total passengers : " + str(total))
                    print(str(id) + " Metro is going to station no. " + str(i + 1) + " direction " + str(
                        direction[int(metro_direc) + 1]))

                elif j > 1:
                    arriving_passengers = random.randrange(1, 300)
                    # leaving_passengers = random.randrange(1, arriving_passengers)
                    leaving_passengers = random.randrange(1, total)
                    # if (arriving_passengers + waiting_passengers) > 250:
                    if (arriving_passengers + waiting_passengers) > (250 - total + leaving_passengers):
                        # waiting_passengers = arriving_passengers - 250
                        waiting_passengers = arriving_passengers + waiting_passengers - 250 - total
                        arriving_passengers = arriving_passengers - waiting_passengers
                        print("The arriving passenger are " + str(arriving_passengers) + " waiting passenger are " + str(
                            waiting_passengers))
                        print("The leaving passengers are " + str(leaving_passengers))
                        total = total + arriving_passengers - leaving_passengers
                        print("total passengers : " + str(total))
                    else:
                        # total = total + arriving_passengers - leaving_passengers
                        total = total + arriving_passengers + waiting_passengers - leaving_passengers
                        print("total passengers : " + str(total))
                        print("The arriving passenger are " + str(arriving_passengers) + " leaving passenger are " + str(
                            leaving_passengers))
                else:
                    # leaving_passengers = random.randrange(1, 250)
                    leaving_passengers = total
                    arriving_passengers = 0
                    # total = total - leaving_passengers
                    total = 0
                    print("total passengers : " + str(total))
                    print("The arriving passengers are " + str(
                        arriving_passengers) + " and the leaving passengers are " + str(
                        leaving_passengers))
                j = j - 1


print("WELCOME TO THE METRO MANAGER- ENJOY YOUR METRO EXPERIENCE")
print("-----------------------------------------------------------")
train = Metro()
id, total = train.metro_id()
print("The metro id is " + str(id))
metro_direc = train.Metro_direction()
stationum = train.Station()
print("---------------------------------------")
train.Movingtrain(id, stationum, metro_direc, total)
train2 = Metro()
id1, total = train2.metro_id()
print("The metro id is " + str(id1))
metro_direc = train.Metro_direction()
stationum = train2.Station()
print("---------------------------------------")
train2.Movingtrain(id, stationum, metro_direc, total)
