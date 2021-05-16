# ----------------------------------------------------------
# FINAL PROJECT
# Written BY :-  Jaya Shree (2093410) & Tarandeep Singh (2094291)
# -----------------------------------------------------------

# datetime module used to find the current time
from datetime import *
# calendar module used to find the day
import calendar
# reduce function used to apply a particular function passed in its arguments to all of the list elements
from functools import reduce
# prettytable module is used to draw the tabular column
from prettytable import *


# This method is used to find the list of values within the given value
def cheaperThan(self):
    sampleList = self.costList
    cheap = int(input("Enter the value: "))
    sampleList.append(cheap)
    sampleList.sort()
    for i in sampleList:
        if i == cheap:
            break
        else:
            print(i)

        # This method is used to find the highest price


def highestPrice(self):
    self.sortCost.sort()  # sort the list
    self.sizeStr = -1
    self.highLowDet(
        self.sizeStr)  # calling the function to print the details of pizza with an argument of size which is found at the above line


# This method is used to find the lowest price
def lowestPrice(self):
    self.sortCost.sort()  # sort the list
    self.sizeStr = 0
    self.highLowDet(
        self.sizeStr)  # calling the function to print the details of pizza with an argument of size which is found at the above line


# Main class
class Pizza():
    # Constructor of class Pizza
    def __init__(self):
        # Welcome message by program
        print()
        print("            Welcome to Papa John's Pizza ")
        print("            **********************************")
        print()
        print("**  Order through our app to get 10% Off  **")
        print("Download our app in the Playstore/Appstore and enjoy the offer")
        print()
        todayDate = date.today()  # to find the today's date
        self.day = calendar.day_name[todayDate.weekday()]  # to find the day

        todayDate = todayDate.strftime("%d-%m-%y")  # date will be in the form of DD/MM/YY
        print("Today's date:", todayDate + ",", self.day)  # printing date and day
        print()
        while True:
            self.mobApp = input(
                " Would you like to download our app: ")  # to find whether the user ordering from mobile or offline
            if self.mobApp == "y":
                break
            elif self.mobApp == "n":
                break
            else:
                print("Please select (y/n) alone")
                continue
        print()

        self.todaysPizzas = []  # list, with number of pizzas that could be made by Papa John
        print()
        pizzaCount = int(input("How many pizzas can you make today: "))

        i = 0
        while i < pizzaCount:
            self.todaysPizzas.append(i)  # append the numbers into today's Pizzas list
            i = i + 1

    # This method is used to store the size and cost of the pizza
    def getSize(self):
        self.sizeList = []
        self.sizeCost = []
        self.sortCost = []

    # This method is used to get the size info from the user
    def setSize(self):
        while True:
            self.pizzaSize = input("Size ( s/m/l ): ")
            if self.pizzaSize == "s" or self.pizzaSize == "m" or self.pizzaSize == "l":
                break
            else:
                print("Please select the given sizes")
                continue

        self.sizeList.append(self.pizzaSize)  # Pizza size will append to the size list

    # This method used to store the cheese stuff
    def getStuffedWithCheese(self):
        self.cheeseDoughList = []

    # This method is used to get the cheese stuff info from the user
    def setStuffedWithCheese(self):
        while True:
            self.cheeseDough = input("Cheese in dough ( y/n ): ")

            # 1 and 0 is used to return the output as boolean value True/False
            if self.cheeseDough == 'y':
                self.cheeseDoughList.append(1)  # 1 states - yes --------
                break  # \
                #                          -------> This value will append to the cheese dough list
            elif self.cheeseDough == 'n':  # /
                self.cheeseDoughList.append(0)  # 0 states - no  --------
                break

            else:
                print("Please select the correct option ( y/n ): ")
                continue

    # This method used to store the cheese toppings count and cost
    def getCheese(self):
        self.cheeseToppingsList = []
        self.cheeseToppingsCost = []

    # This method is used to get the cheese count info from the user
    def setCheese(self):
        self.cheeseToppings = int(input("Number of cheese toppings: "))
        self.cheeseToppingsList.append(self.cheeseToppings)  # append the count to the list

        # each count will be multiplied by 2 (cost of each topping)
        self.cheeseToppings = self.cheeseToppings * 2
        self.cheeseToppingsCost.append(self.cheeseToppings)  # append the cost to the list

    # This method used to store the pepperoni toppings count and cost
    def getPepperoni(self):
        self.pepperoniToppingsList = []
        self.pepperoniToppingsCost = []

    # This method is used to get the pepperoni count info from the user
    def setPepperoni(self):
        self.pepperoniToppings = int(input("Number of pepperoni toppings: "))
        self.pepperoniToppingsList.append(self.pepperoniToppings)  # append the count to the list

        # each count will be multiplied by 2 (cost of each topping)
        self.pepperoniToppings = self.pepperoniToppings * 2
        self.pepperoniToppingsCost.append(self.pepperoniToppings)  # append the cost to the list

    # This method used to store the mushroom toppings count and cost
    def getMushroom(self):
        self.mushroomToppingsList = []
        self.mushroomToppingsCost = []

    # This method is used to get the mushroom count info from the user
    def setMushroom(self):
        self.mushroomToppings = int(input("Number of mushroom toppings: "))
        self.mushroomToppingsList.append(self.mushroomToppings)  # append the count to the list

        # each count will be multiplied by 2 (cost of each topping)
        self.mushroomToppings = self.mushroomToppings * 2
        self.mushroomToppingsCost.append(self.mushroomToppings)  # append the cost to the list

    # This method used to store the veggie toppings count and cost
    def getVeggie(self):
        self.veggieToppingsList = []
        self.veggieToppingsCost = []

    # This method is used to get the veggie count info from the user
    def setVeggie(self):
        self.veggieToppings = int(input("Number of veggie toppings: "))
        self.veggieToppingsList.append(self.veggieToppings)  # append the count to the list

        # each count will be multiplied by 2 (cost of each topping)
        self.veggieToppings = self.veggieToppings * 2
        self.veggieToppingsCost.append(self.veggieToppings)  # append the cost to the list

    # This method used to store the cost
    def calcCost(self):
        self.costList = []

    # This method is used to calculate the cost
    def setCalcCost(self):
        if self.pizzaSize == 's':
            self.sizeCost.append(10)  # Cost of small size  - $10 -----
        elif self.pizzaSize == 'm':  # |
            self.sizeCost.append(
                12)  # Cost of medium size - $12 -----------> This cost will append to the size cost list
        elif self.pizzaSize == 'l':  # |
            self.sizeCost.append(14)  # Cost of large size  - $14 -----
        r = self.nums - 1

        # adding all the values using index which is present in all the list mentioned below
        self.cost = int(self.sizeCost[r]) + int(self.cheeseToppingsCost[r]) + int(self.pepperoniToppingsCost[r]) + int(
            self.mushroomToppingsCost[r]) + int(self.veggieToppingsCost[r])

        self.costList.append(self.cost)  # append the total into cost list
        self.sortCost.append(self.cost)
        print("cost : $", self.cost)

    # This method is used to print the details about the pizza using size
    def pizzasOfSize(self, string):
        self.string = self.sizeList[string]
        if self.string not in self.sizeList:  # check whether the size is there in the list or not
            print("There is no pizza order of size", self.string.upper(), "in the list")

        else:
            pizzaIndex = string
            pizzaBoolean = bool(self.cheeseDoughList[pizzaIndex])  # find the boolean value True/False

            # Details of pizza
            print("Pizza #", pizzaIndex + 1)
            print("Pizza size :", self.string.upper())
            print("Cheese filled dough :", pizzaBoolean)
            print("Number of cheese toppings :", self.cheeseToppingsList[pizzaIndex])
            print("Number of pepperoni toppings :", self.pepperoniToppingsList[pizzaIndex])
            print("Number of mushroom toppings :", self.mushroomToppingsList[pizzaIndex])
            print("Number of veggie toppings :", self.veggieToppingsList[pizzaIndex])
            print("Cost : $", self.costList[pizzaIndex])

    def highLowDet(self, sizeStr):
        sizeString = self.sizeList[self.sizeStr]
        pizzaBoolean = bool(self.cheeseDoughList[self.sizeStr])  # find the boolean value True/False

        # Details of pizza
        print("Pizza size :", sizeString.upper())
        print("Cheese filled dough :", pizzaBoolean)
        print("Number of cheese toppings :", self.cheeseToppingsList[self.sizeStr])
        print("Number of pepperoni toppings :", self.pepperoniToppingsList[self.sizeStr])
        print("Number of mushroom toppings :", self.mushroomToppingsList[self.sizeStr])
        print("Number of veggie toppings :", self.veggieToppingsList[self.sizeStr])
        print("Cost : $", self.costList[self.sizeStr])

    # This method is used to change the size
    def sizeChange(self):
        self.modifiedVal = input("Enter the size (to replace old size): ")  # new size
        self.sizeList.remove(self.sizeList[self.stringIndex])  # remove the old size

    # This method is used to change the cheese dough
    def cheeseDoughChange(self):
        oldCheese = input("Enter the cheese dough (to replace old option): ")  # new value
        if oldCheese == 'y':
            self.modifiedVal = 1
        elif oldCheese == 'n':
            self.modifiedVal = 0
        self.cheeseDoughList.remove(self.cheeseDoughList[self.stringIndex])  # remove the old value

    # This method is used to change the cheese counting
    def cheeseChange(self):
        self.modifiedVal = int(input("Enter the number of cheese (to replace old cheese total): "))  # new value
        self.cheeseToppingsList.remove(self.cheeseToppingsList[self.stringIndex])  # remove the old value
        self.cheeseToppingsCost.remove(self.cheeseToppingsCost[self.stringIndex])

        # This method is used to change the pepperoni counting

    def pepperoniChange(self):
        self.modifiedVal = int(input("Enter the number of pepperoni (to replace old pepperoni total): "))  # new value
        self.pepperoniToppingsList.remove(self.pepperoniToppingsList[self.stringIndex])  # remove the old value
        self.pepperoniToppingsCost.remove(self.pepperoniToppingsCost[self.stringIndex])  # remove the old cost

    # This method is used to change the mushroom counting
    def mushroomChange(self):
        self.modifiedVal = int(input("Enter the number of mushroom (to replace old mushroom total): "))  # new value
        self.mushroomToppingsList.remove(self.mushroomToppingsList[self.stringIndex])  # remove the old value
        self.mushroomToppingsCost.remove(self.mushroomToppingsCost[self.stringIndex])  # remove the old cost

    # This method is used to change the veggie counting
    def veggieChange(self):
        self.modifiedVal = int(input("Enter the number of veggie (to replace old veggie total): "))  # new value
        self.veggieToppingsList.remove(self.veggieToppingsList[self.stringIndex])  # remove the old value
        self.veggieToppingsCost.remove(self.veggieToppingsCost[self.stringIndex])  # remove the old cost

    # This method is used to check the password
    def passwordChecker(self):
        print()
        print("**  Only 3 chances  **")  # user has only three chance
        print()
        for j in range(1, 4):
            password = input("password: ")
            if password == "deluxepizza":
                break
            else:
                print("Sorry your password is incorrect")
                if j == 3:
                    print()
                    print("**  Please type the correct password  **")
                    print()
                    self.__str__()

    # This method is just made to overcome the Attribute error
    def justCheck(self):
        self.getSize()
        self.getStuffedWithCheese()
        self.getCheese()
        self.getPepperoni()
        self.getMushroom()
        self.getVeggie()
        self.calcCost()

    # This method is used to collect the info from the user
    def setValues(self):
        self.setSize()
        self.setStuffedWithCheese()
        self.setCheese()
        self.setPepperoni()
        self.setMushroom()
        self.setVeggie()
        self.setCalcCost()

    # Overwritting the str method
    def __str__(self):
        self.justCheck()
        while True:
            # Main menu
            print()
            print("Papa John, what do you want to do...?")
            print("    1. Enter a new pizza order ( password required )")
            print("    2. Change information of a specific order ( password required )")
            print("    3. Display details for all pizzas of a specific size ( s/m/l )")
            print("    4. Statistics on today's pizzas")
            print("    5. Quit")
            option = int(input("Please enter your choice: "))

            if option == 1:
                self.passwordChecker()  # to check the password
                while True:
                    ability = len(self.todaysPizzas)  # length of today's Pizzas list
                    numOfPizzas = int(input("\nHow many pizzas are in this order ? "))
                    if numOfPizzas > ability:  # check whether it is beyond the limit (today's Pizza)
                        print("Sorry you have insufficient amount of ingredients", ability, "numbers of pizzas only")
                        continue
                    else:
                        break

                # Getting info from user
                self.nums = 1
                while True:
                    print()
                    print("Pizza number", self.nums)
                    self.setValues()  # this function will run all the functions in it
                    self.nums = self.nums + 1
                    if self.nums > numOfPizzas:
                        break
                    else:
                        pass

            # Changing pizza's info
            elif option == 2:
                print()
                self.passwordChecker()  # to check password
                print()

                # Print all the pizzas size ordered by user
                num = 1
                for v in self.sizeList:
                    print("Pizza", num, "-", v)
                    num = num + 1

                print()
                print("Please type the number (don't type size)")
                self.string = int(input("Which pizza do you wish to modify: "))  # size, to change info of that
                self.u = self.sizeList[self.string - 1]

                # Check whether the size is there or not
                if self.u not in self.sizeList:
                    print("There is no pizza order of size", self.u.upper(), "in the list")
                    continue

                self.pizzasOfSize(self.string - 1)  # print the detail of that pizza
                self.stringIndex = self.sizeList.index(self.string)  # find the index of that pizza

                # User can change the anything mentioned below
                while True:
                    print()
                    print("John, what would you like to change: ")
                    print("    1. Size")
                    print("    2. Cheese filled or not")
                    print("    3. Number of cheese toppings")
                    print("    4. Number of pepperoni toppings")
                    print("    5. Number of mushroom toppings")
                    print("    6. Number of veggie toppings")
                    print("    7. Quit")
                    option = int(input("Enter your choice> "))

                    # Size changing
                    if option == 1:
                        self.sizeChange()  # function helps to get new size from user
                        self.sizeList.insert(self.stringIndex, self.modifiedVal)  # insert new size into sizeList
                        if self.modifiedVal == 's':
                            self.new = 10
                        elif self.modifiedVal == 'm':
                            self.new = 12
                        elif self.modifiedVal == 'l':
                            self.new = 14
                        if self.string == 's':
                            oldCost = self.costList[self.stringIndex]
                            oldCost = oldCost - 10
                            self.newCost = self.new + oldCost
                            self.costList.remove(self.costList[self.stringIndex])  # remove the old cost
                            self.costList.insert(self.stringIndex, self.newCost)
                            self.sortCost.remove(self.sortCost[self.stringIndex])
                            self.sortCost.insert(self.stringIndex, self.newCost)
                        elif self.string == 'm':
                            oldCost = self.costList[self.stringIndex]
                            oldCost = oldCost - 12
                            self.newCost = self.new + oldCost
                            self.costList.remove(self.costList[self.stringIndex])  # remove the old cost
                            self.costList.insert(self.stringIndex, self.newCost)  # add new cost
                            self.sortCost.remove(self.sortCost[self.stringIndex])
                            self.sortCost.insert(self.stringIndex, self.newCost)
                        elif self.string == 'l':
                            oldCost = self.costList[self.stringIndex]
                            oldCost = oldCost - 14
                            self.newCost = self.new + oldCost
                            self.costList.remove(self.costList[self.stringIndex])  # remove the old cost
                            self.costList.insert(self.stringIndex, self.newCost)  # add new cost
                            self.sortCost.remove(self.sortCost[self.stringIndex])
                            self.sortCost.insert(self.stringIndex, self.newCost)

                        # cheese dough changing
                    elif option == 2:
                        self.cheeseDoughChange()
                        self.cheeseDoughList.insert(self.stringIndex, self.modifiedVal)

                    # changing cheese toppings count
                    elif option == 3:
                        self.cheeseChange()
                        self.cheeseToppingsList.insert(self.stringIndex, self.modifiedVal)
                        self.costList.remove(self.costList[self.stringIndex])
                        self.modifiedVal = self.modifiedVal * 2
                        self.cheeseToppingsCost.insert(self.stringIndex, self.modifiedVal)
                        self.cost = int(self.sizeCost[self.stringIndex]) + int(
                            self.cheeseToppingsCost[self.stringIndex]) + int(
                            self.pepperoniToppingsCost[self.stringIndex]) + int(
                            self.mushroomToppingsCost[self.stringIndex]) + int(
                            self.veggieToppingsCost[self.stringIndex])
                        self.costList.insert(self.stringIndex, self.cost)
                        self.sortCost.remove(self.sortCost[self.stringIndex])
                        self.sortCost.insert(self.stringIndex, self.cost)

                    # changing pepperoni toppings count
                    elif option == 4:
                        self.pepperoniChange()
                        self.pepperoniToppingsList.insert(self.stringIndex, self.modifiedVal)
                        self.costList.remove(self.costList[self.stringIndex])
                        self.modifiedVal = self.modifiedVal * 2
                        self.pepperoniToppingsCost.insert(self.stringIndex, self.modifiedVal)
                        self.cost = int(self.sizeCost[self.stringIndex]) + int(
                            self.cheeseToppingsCost[self.stringIndex]) + int(
                            self.pepperoniToppingsCost[self.stringIndex]) + int(
                            self.mushroomToppingsCost[self.stringIndex]) + int(
                            self.veggieToppingsCost[self.stringIndex])
                        self.costList.insert(self.stringIndex, self.cost)
                        self.sortCost.remove(self.sortCost[self.stringIndex])
                        self.sortCost.insert(self.stringIndex, self.cost)

                    # changing mushroom toppings count
                    elif option == 5:
                        self.mushroomChange()
                        self.mushroomToppingsList.insert(self.stringIndex, self.modifiedVal)
                        self.costList.remove(self.costList[self.stringIndex])
                        self.modifiedVal = self.modifiedVal * 2
                        self.mushroomToppingsCost.insert(self.stringIndex, self.modifiedVal)
                        self.cost = int(self.sizeCost[self.stringIndex]) + int(
                            self.cheeseToppingsCost[self.stringIndex]) + int(
                            self.pepperoniToppingsCost[self.stringIndex]) + int(
                            self.mushroomToppingsCost[self.stringIndex]) + int(
                            self.veggieToppingsCost[self.stringIndex])
                        self.costList.insert(self.stringIndex, self.cost)
                        self.sortCost.remove(self.sortCost[self.stringIndex])
                        self.sortCost.insert(self.stringIndex, self.cost)


                    # changing veggie toppings count
                    elif option == 6:
                        self.veggieChange()
                        self.veggieToppingsList.insert(self.stringIndex, self.modifiedVal)
                        self.costList.remove(self.costList[self.stringIndex])
                        self.modifiedVal = self.modifiedVal * 2
                        self.veggieToppingsCost.insert(self.stringIndex, self.modifiedVal)
                        self.cost = int(self.sizeCost[self.stringIndex]) + int(
                            self.cheeseToppingsCost[self.stringIndex]) + int(
                            self.pepperoniToppingsCost[self.stringIndex]) + int(
                            self.mushroomToppingsCost[self.stringIndex]) + int(
                            self.veggieToppingsCost[self.stringIndex])
                        self.costList.insert(self.stringIndex, self.cost)
                        self.sortCost.remove(self.sortCost[self.stringIndex])
                        self.sortCost.insert(self.stringIndex, self.cost)


                    elif option == 7:
                        break

                    else:
                        print("Read the options carefully")
                        continue

                    # Printing details individually
            elif option == 3:
                # Print all the pizzas size ordered by user
                num = 1
                for v in self.sizeList:
                    print("Pizza", num, "-", v)
                    num = num + 1
                print("Please type the number (dont type the size)")
                self.string = int(input("\nJohn, what size pizza do you want a list of: "))
                self.g = self.string - 1
                self.string = self.g
                self.pizzasOfSize(self.string)


            elif option == 4:
                while True:
                    print("\nJohn, what information would you like ?")
                    print("\t1. Cost and details of cheapest pizza")
                    print("\t2. Cost and details of most costly pizza")
                    print("\t3. Number of pizzas sold today")
                    print("\t4. Number of pizzas of a specific size")
                    print("\t5. Average cost of pizzas")
                    print("\t6. Quit")
                    option = int(input("Enter your choice > "))

                    # Lowest price
                    if option == 1:
                        print()
                        lowestPrice(self)

                    # Highest price
                    elif option == 2:
                        print()
                        highestPrice(self)

                    # Find number of pizzas sold today
                    elif option == 3:
                        print()
                        print("Number of pizzas sold today is", len(self.sizeList))

                    # find count using specific size
                    elif option == 4:
                        num = 1
                        for v in self.sizeList:
                            print("Pizza", num, "-", v)
                            num = num + 1
                        print()
                        print("Please type the number (dont type the number)")
                        self.specificSizeFind = int(input("What size pizza do you want: "))
                        b = self.sizeList[self.specificSizeFind - 1]
                        specificSizeCount = self.sizeList.count(b)
                        print("Total number of", b, "sized pizzas made today is", specificSizeCount)
                        self.string = self.specificSizeFind - 1
                        self.pizzasOfSize(self.string)

                    # Average
                    elif option == 5:
                        red = reduce(lambda x, y: x + y, self.costList)
                        lenOfCostList = len(self.costList)
                        avg = red / lenOfCostList
                        print("Average cost of pizzas sold today is $", round(avg, 2))

                    elif option == 6:
                        break

                    else:
                        print("Please select the correct option")

            # Final part with bill
            elif option == 5:
                print()
                # Weekly offer
                if self.day == "Monday":  # this is mutable
                    print("Congratulations, today weekly offer day")
                    # Weekly special table
                    print()
                    print("**    Monday SPECIAL    **")
                    print("      ``````````````")
                    weeKlyspl = PrettyTable(["S.No", "Specials"])
                    weeKlyspl.add_row(["1.", "Choco shake"])
                    weeKlyspl.add_row(["2.", "Choco lave cake"])
                    print(weeKlyspl)
                    print()
                    print("Please type the name, dont type the numbers")
                    print()
                    lst = ["choco lava cake", "choco shake"]
                    while True:
                        splOff = input("Choose your favourite: ")

                        # checking whether it is there or not
                        if splOff.lower() not in lst:
                            print("please type from the above menu card ")
                            continue
                        else:
                            break

                        # check whether user using mobile app or not
                if self.mobApp == 'y':
                    # discount part
                    splOff = ""
                    totalRed = reduce(lambda q, r: q + r, self.costList)
                    red = totalRed / 100
                    off = red * 10
                    weeklyOff = totalRed - off
                    print()

                    # Bill table
                    print("**  Bill  **")
                    print("    ````")
                    offTab = PrettyTable(["Pizza Qty", "Offer", "Discount", "Cost ($)"])
                    offTab.add_row([len(self.sizeList), splOff, "10%", weeklyOff])
                    print(offTab)

                # No mobile app
                else:
                    if self.day != "Monday":
                        splOff = "-"

                    # Bill table
                    red = int(reduce(lambda q, r: q + r, self.costList))
                    tab = PrettyTable(["Pizza Qty", "Offer", "Discount", "Cost ($)"])
                    tab.add_row([len(self.sizeList), splOff, "-", red])
                    print(tab)

                # Rating table part
                print()
                print("**  Please rate our service  **")
                print("    ```````````````````````")
                print()

                while True:
                    print("Please type the numbers instead alphabets")
                    print()
                    rating = int(input("Give your rating (1-5): "))
                    if rating > 5:
                        print("Please rate within 5")
                        continue

                    break

                print()
                rat = PrettyTable(["S.No", "User Rating"])
                rat.add_row(["1.", rating])
                print(rat)
                print()
                print("Thanks for rating our service")
                exit()

            else:
                print("Please enter a correct option")

            continue


DeluxePizza = Pizza()  # object for class Pizza

print(DeluxePizza)
