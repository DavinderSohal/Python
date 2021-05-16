import calendar
from datetime import *
from functools import reduce


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


def highestPrice(self):
    self.costList.sort()
    self.sortedList = self.costList[-1]
    highInd = self.costList.index(self.sortedList)
    self.string = self.sizeList[highInd]
    self.pizzasOfSize(self.string)


def lowestPrice(self):
    print(self.costList)
    self.costList.sort()
    self.sortedList = self.costList[0]
    lowInd = self.costList.index(self.sortedList)
    self.string = self.sizeList[lowInd]
    self.pizzasOfSize(self.string)


class Pizza():
    def __init__(self):
        print()
        print("            Welcome to Papa John's Pizzaspot  ")
        print("            ````````````````````````````````")
        print()
        print("**  Order through our app to get 10% Off  **")
        print("Download our app in the playstore and enjoy the offer")
        print()
        self.mobApp = input("Are you like to download our app: ")
        print()
        todayDate = date.today()
        day = calendar.day_name[todayDate.weekday()]

        todayDate = todayDate.strftime("%d-%m-%y")
        print("Today's date:", todayDate + ",", day)
        if day == "Sunday":
            print()
            print("-------------------------------------")
            print("     **    Sunday SPECIAL    **")
            print("           ``````````````")
            print("   Today offer - Buy 1 Get 1 free")
            print("-------------------------------------")
            print()

            print("congratulations, today weekly offer day, so enjoy the offer and rate our service")

        self.todaysPizzas = []
        print()
        pizzaCount = int(input("How many pizzas can you make today: "))

        i = 0
        while i < pizzaCount:
            self.todaysPizzas.append(i)
            i = i + 1

    def getSize(self):
        self.sizeList = []
        self.sizeCost = []

    def setSize(self):
        self.pizzaSize = input("Size ( s/m/l ): ")
        if self.pizzaSize == 's':
            self.sizeCost.append(10)
        elif self.pizzaSize == 'm':
            self.sizeCost.append(12)
        elif self.pizzaSize == 'l':
            self.sizeCost.append(14)
        self.sizeList.append(self.pizzaSize)

    def getStuffedWithCheese(self):
        self.cheeseDoughList = []

    def setStuffedWithCheese(self):
        while True:
            self.cheeseDough = input("Cheese in dough ( y/n ): ")
            if self.cheeseDough == 'y':
                self.cheeseDoughList.append(1)
                break
            elif self.cheeseDough == 'n':
                self.cheeseDoughList.append(0)
                break
            else:
                print("Please select the correct option ( y/n ): ")
                continue

    def getCheese(self):
        self.cheeseToppingsList = []
        self.cheeseToppingsCost = []

    def setCheese(self):
        self.cheeseToppings = int(input("Number of cheese toppings: "))
        self.cheeseToppingsList.append(self.cheeseToppings)
        self.cheeseToppings = self.cheeseToppings * 2
        self.cheeseToppingsCost.append(self.cheeseToppings)

    def getPepperoni(self):
        self.pepperoniToppingsList = []
        self.pepperoniToppingsCost = []

    def setPepperoni(self):
        self.pepperoniToppings = int(input("Number of pepperoni toppings: "))
        self.pepperoniToppingsList.append(self.pepperoniToppings)
        self.pepperoniToppings = self.pepperoniToppings * 2
        self.pepperoniToppingsCost.append(self.pepperoniToppings)

    def getMushroom(self):
        self.mushroomToppingsList = []
        self.mushroomToppingsCost = []

    def setMushroom(self):
        self.mushroomToppings = int(input("Number of mushroom toppings: "))
        self.mushroomToppingsList.append(self.mushroomToppings)
        self.mushroomToppings = self.mushroomToppings * 2
        self.mushroomToppingsCost.append(self.mushroomToppings)

    def getVeggie(self):
        self.veggieToppingsList = []
        self.veggieToppingsCost = []

    def setVeggie(self):
        self.veggieToppings = int(input("Number of veggie toppings: "))
        self.veggieToppingsList.append(self.veggieToppings)
        self.veggieToppings = self.veggieToppings * 2
        self.veggieToppingsCost.append(self.veggieToppings)

    def calcCost(self):
        self.costList = []

    def setCalcCost(self):
        r = self.sizeList.index(self.pizzaSize)
        self.cost = int(self.sizeCost[r]) + int(self.cheeseToppingsCost[r]) + int(self.pepperoniToppingsCost[r]) + int(
            self.mushroomToppingsCost[r]) + int(self.veggieToppingsCost[r])

        self.costList.append(self.cost)
        print("cost : $", self.cost)

    def pizzasOfSize(self, string):
        print()
        if self.string not in self.sizeList:
            print("There is no pizza order of size", self.string.upper(), "in the list")

        else:
            pizzaIndex = self.sizeList.index(self.string)
            print("index ", pizzaIndex)
            pizzaBoolean = bool(self.cheeseDoughList[pizzaIndex])
            print("Pizza #", pizzaIndex + 1)
            print("Pizza size :", self.string.upper())
            print("Cheese filled dough :", pizzaBoolean)
            print("Number of cheese toppings :", self.cheeseToppingsList[pizzaIndex])
            print("Number of pepperoni toppings :", self.pepperoniToppingsList[pizzaIndex])
            print("Number of mushroom toppings :", self.mushroomToppingsList[pizzaIndex])
            print("Number of veggie toppings :", self.veggieToppingsList[pizzaIndex])
            print("Cost : $", self.costList[pizzaIndex])

    def sizeChange(self):
        self.modifiedVal = input("Enter the size (to replace old size): ")
        self.sizeList.remove(self.sizeList[self.stringIndex])

    def cheeseDoughChange(self):
        oldCheese = input("Enter the cheese dough (to replace old option): ")
        if oldCheese == 'y':
            self.modifiedVal = 1
        elif oldCheese == 'n':
            self.modifiedVal = 0
        self.cheeseDoughList.remove(self.cheeseDoughList[self.stringIndex])

    def cheeseChange(self):
        self.modifiedVal = int(input("Enter the number of cheese (to replace old cheese total): "))
        self.cheeseToppingsList.remove(self.cheeseToppingsList[self.stringIndex])
        self.cheeseToppingsCost.remove(self.cheeseToppingsCost[self.stringIndex])

    def pepperoniChange(self):
        self.modifiedVal = int(input("Enter the number of pepperoni (to replace old pepperoni total): "))
        self.pepperoniToppingsList.remove(self.pepperoniToppingsList[self.stringIndex])
        self.pepperoniToppingsCost.remove(self.pepperoniToppingsCost[self.stringIndex])

    def mushroomChange(self):
        self.modifiedVal = int(input("Enter the number of mushroom (to replace old mushroom total): "))
        self.mushroomToppingsList.remove(self.mushroomToppingsList[self.stringIndex])
        self.mushroomToppingsCost.remove(self.mushroomToppingsCost[self.stringIndex])

    def veggieChange(self):
        self.modifiedVal = int(input("Enter the number of veggie (to replace old veggie total): "))
        self.veggieToppingsList.remove(self.veggieToppingsList[self.stringIndex])
        self.veggieToppingsCost.remove(self.veggieToppingsCost[self.stringIndex])

    def passwordChecker(self):
        print("**  Only 3 chances  **")
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

    def justCheck(self):
        self.getSize()
        self.getStuffedWithCheese()
        self.getCheese()
        self.getPepperoni()
        self.getMushroom()
        self.getVeggie()
        self.calcCost()

    def setValues(self):
        self.setSize()
        self.setStuffedWithCheese()
        self.setCheese()
        self.setPepperoni()
        self.setMushroom()
        self.setVeggie()
        self.setCalcCost()

    def __str__(self):
        self.justCheck()
        while True:
            print()
            print("Papa John, what do you want to do...?")
            print("    1. Enter a new pizza order ( password required )")
            print("    2. Change information of a specific order ( password required )")
            print("    3. Display details for all pizzas of a specific size ( s/m/l )")
            print("    4. Statistics on today's pizzas")
            print("    5. Quit")
            option = int(input("Please enter your choice: "))

            if option == 1:
                self.passwordChecker()
                while True:
                    ability = len(self.todaysPizzas)
                    numOfPizzas = int(input("\nHow many pizzas are in this order ? "))
                    if numOfPizzas > ability:
                        print("Sorry I have less ingrediants to make", ability, "numbers of pizzas only")
                        continue
                    else:
                        break

                nums = 1
                while True:
                    print()
                    print("Pizza number", nums)
                    self.setValues()
                    nums = nums + 1
                    if nums > numOfPizzas:
                        break
                    else:
                        pass


            elif option == 2:
                print()
                self.passwordChecker()
                self.string = input("Which pizza do you wish to modify: ")
                if self.string not in self.sizeList:
                    print("There is no pizza order of size", self.string.upper(), "in the list")
                    continue
                self.pizzasOfSize(self.string)
                self.stringIndex = self.sizeList.index(self.string)
                print()
                print("John, what would you like to change: ")
                print("    1. Size")
                print("    2. Cheese filled or not")
                print("    3. Number of cheese topppings")
                print("    4. Number of pepperoni topppings")
                print("    5. Number of mushroom topppings")
                print("    6. Number of veggie topppings")
                print("    7. Quit")
                option = int(input("Enter your choice> "))
                if option == 1:
                    self.sizeChange()
                    self.sizeList.insert(self.stringIndex, self.modifiedVal)
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
                        self.costList.insert(self.stringIndex, self.newCost)
                    elif self.string == 'm':
                        oldCost = self.costList[self.stringIndex]
                        oldCost = oldCost - 12
                        self.newCost = self.new + oldCost
                        self.costList.insert(self.stringIndex, self.newCost)
                    elif self.string == 'l':
                        oldCost = self.costList[self.stringIndex]
                        oldCost = oldCost - 14
                        self.newCost = self.new + oldCost
                        self.costList.insert(self.stringIndex, self.newCost)

                elif option == 2:
                    self.cheeseDoughChange()
                    self.cheeseDoughList.insert(self.stringIndex, self.modifiedVal)

                elif option == 3:
                    self.cheeseChange()
                    self.cheeseToppingsList.insert(self.stringIndex, self.modifiedVal)
                    self.modifiedVal = self.modifiedVal * 2
                    self.cheeseToppingsCost.insert(self.stringIndex, self.modifiedVal)
                    self.pizzaSize = self.string
                    self.cost = int(self.sizeCost[self.stringIndex]) + int(
                        self.cheeseToppingsCost[self.stringIndex]) + int(
                        self.pepperoniToppingsCost[self.stringIndex]) + int(
                        self.mushroomToppingsCost[self.stringIndex]) + int(self.veggieToppingsCost[self.stringIndex])
                    self.costList.insert(self.stringIndex, self.cost)

                elif option == 4:
                    self.pepperoniChange()
                    self.pepperoniToppingsList.insert(self.stringIndex, self.modifiedVal)
                    self.modifiedVal = self.modifiedVal * 2
                    self.pepperoniToppingsCost.insert(self.stringIndex, self.modifiedVal)
                    self.pizzaSize = self.string
                    self.cost = int(self.sizeCost[self.stringIndex]) + int(
                        self.cheeseToppingsCost[self.stringIndex]) + int(
                        self.pepperoniToppingsCost[self.stringIndex]) + int(
                        self.mushroomToppingsCost[self.stringIndex]) + int(self.veggieToppingsCost[self.stringIndex])
                    self.costList.insert(self.stringIndex, self.cost)


                elif option == 5:
                    self.mushroomChange()
                    self.mushroomToppingsList.insert(self.stringIndex, self.modifiedVal)
                    self.modifiedVal = self.modifiedVal * 2
                    self.mushroomToppingsCost.insert(self.stringIndex, self.modifiedVal)
                    self.pizzaSize = self.string
                    self.cost = int(self.sizeCost[self.stringIndex]) + int(
                        self.cheeseToppingsCost[self.stringIndex]) + int(
                        self.pepperoniToppingsCost[self.stringIndex]) + int(
                        self.mushroomToppingsCost[self.stringIndex]) + int(self.veggieToppingsCost[self.stringIndex])
                    self.costList.insert(self.stringIndex, self.cost)



                elif option == 6:
                    self.veggieChange()
                    self.veggieToppingsList.insert(self.stringIndex, self.modifiedVal)
                    self.modifiedVal = self.modifiedVal * 2
                    self.veggieToppingsCost.insert(self.stringIndex, self.modifiedVal)
                    self.pizzaSize = self.string
                    self.cost = int(self.sizeCost[self.stringIndex]) + int(
                        self.cheeseToppingsCost[self.stringIndex]) + int(
                        self.pepperoniToppingsCost[self.stringIndex]) + int(
                        self.mushroomToppingsCost[self.stringIndex]) + int(self.veggieToppingsCost[self.stringIndex])
                    self.costList.insert(self.stringIndex, self.cost)


                elif option == 7:
                    break

                else:
                    print("Read the options carefully")
                    cheaperThan(self)

            elif option == 3:
                self.string = input("\nJohn, what size pizza do you want a list of (s/m/l) : ")
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
                    if option == 1:
                        print()
                        lowestPrice(self)

                    elif option == 2:
                        print()
                        highestPrice(self)

                    elif option == 3:
                        print()
                        print("Number of pizzas sold today is", len(self.sizeList))

                    elif option == 4:
                        print()
                        self.specificSizeFind = input("What size pizza do you want (s/m/l): ")

                        specificSizeCount = self.sizeList.count(self.specificSizeFind)
                        print("Total number of", self.specificSizeFind, "sized pizzas made today is", specificSizeCount)
                        self.string = self.specificSizeFind
                        self.pizzasOfSize(self.string)

                    elif option == 5:
                        red = reduce(lambda x, y: x + y, self.costList)
                        print(red)
                        lenOfCostList = len(self.costList)
                        print(lenOfCostList)

                        avg = red / lenOfCostList

                        print("Average cost of pizzas sold today is $", round(avg, 2))

                    elif option == 6:
                        break

                    else:
                        print("Please select the correct option")


            elif option == 5:
                if self.mobApp == 'y':

                    totalRed = reduce(lambda q, r: q + r, self.costList)
                    red = totalRed / 100
                    off = red * 10
                    weeklyOff = totalRed - off
                    print("Your bill with weekly offer (including mobile app discount):", weeklyOff)
                else:
                    red = int(reduce(lambda q, r: q + r, self.costList))
                    print("Your bill:", red)

                print("Please rate our service")
                rating = input("Give your rating (1-5): ")
                print("Thanks for rating our service")
                exit()

            else:
                print("Please enter a correct option")

            continue


DeluxePizza = Pizza()

print(DeluxePizza)
