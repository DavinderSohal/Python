import datetime
from statistics import mean

from prettytable import PrettyTable


def highestPrice(self):
    cheapest_pizza = min(self.get_cost)
    cheapest_pizza_index = self.get_cost.index(cheapest_pizza)
    b = bool(self.get_cheese_dough[cheapest_pizza_index])
    print(f"\nPizza # {cheapest_pizza_index + 1} is the cheapest pizza")
    print(f"Pizza size : {self.get_size[cheapest_pizza_index].upper()}")
    print(f"Cheese filled dough : {b}")
    print(f"Number of cheese toppings : {self.get_cheese_toppings[cheapest_pizza_index]}")
    print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[cheapest_pizza_index]}")
    print(f"Number of mushroom toppings : {self.get_mushroom_toppings[cheapest_pizza_index]}")
    print(f"Number of veggie toppings : {self.get_veggie_toppings[cheapest_pizza_index]}")
    print(f"Cost : ${self.get_cost[cheapest_pizza_index]}")


def lowestPrice(self):
    costly_pizza = max(self.get_cost)
    costly_pizza_index = self.get_cost.index(costly_pizza)
    b = bool(self.get_cheese_dough[costly_pizza_index])
    print(f"\nPizza # {costly_pizza_index + 1} is the most costliest pizza")
    print(f"Pizza size : {self.get_size[costly_pizza_index].upper()}")
    print(f"Cheese filled dough : {b}")
    print(f"Number of cheese toppings : {self.get_cheese_toppings[costly_pizza_index]}")
    print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[costly_pizza_index]}")
    print(f"Number of mushroom toppings : {self.get_mushroom_toppings[costly_pizza_index]}")
    print(f"Number of veggie toppings : {self.get_veggie_toppings[costly_pizza_index]}")
    print(f"Cost : ${self.get_cost[costly_pizza_index]}")


class Pizza:
    def __init__(self):
        self.get_size = []
        self.get_cheese_dough = []
        self.get_cheese_toppings = []
        self.get_pepperoni_toppings = []
        self.get_mushroom_toppings = []
        self.get_veggie_toppings = []
        self.get_ice_cream_cost = []
        self.get_ice_cream = []
        self.get_cost = []

    def getSize(self):
        self.size = input("size ( s/m/l ) : ")
        self.get_size.append(self.size)

    def stuffedWithCheesed(self):
        while True:
            self.cheese_dough = input("cheese in dough ( y/n ) : ")
            if self.cheese_dough == 'y':
                self.get_cheese_dough.append(1)
                break
            elif self.cheese_dough == 'n':
                self.get_cheese_dough.append(0)
                break
            else:
                print("Please select the correct option")
                continue

    def getCheese(self):
        self.cheese_toppings = int(input("number of cheese toppings : "))
        self.get_cheese_toppings.append(self.cheese_toppings)

    def getPepperoni(self):
        self.pepperoni_toppings = int(input("number of pepperoni toppings : "))
        self.get_pepperoni_toppings.append(self.pepperoni_toppings)

    def getMushroom(self):
        self.mushroom_toppings = int(input("number of mushroom toppings : "))
        self.get_mushroom_toppings.append(self.mushroom_toppings)

    def getVeggie(self):
        self.veggie_toppings = int(input("number of veggie toppings : "))
        self.get_veggie_toppings.append(self.veggie_toppings)

    def getIceCream(self, i):
        if i == 1:
            print("\nWe have Ice creams too, If you like then just check that also")
        else:
            print("\nDo you want to order ice cream with this pizza also")
        self.ice = input("Press 'y' to check the ice cream menu card : ")
        if self.ice == 'y':
            ice_cream_det = PrettyTable()
            ice_columns = ["ICE CREAM", "Cost ($) small-cup", "Cost ($) large-cup"]
            ice_cream_det.add_column(ice_columns[0], ["Chocolate", "Strawberry", "Mix fruit", "Vennila"])
            ice_cream_det.add_column(ice_columns[1], ["4", "4", "4", "4"])
            ice_cream_det.add_column(ice_columns[2], ["8", "8", "8", "8"])
            print(ice_cream_det)
            ice_avail_list = ["chocolate", "strawberry", "mix fruit", "vennila"]
            while True:
                ice_flavour = input("Choose your flavour : ")
                if ice_flavour.lower() not in ice_avail_list:
                    print("Please choose the flavour which are mentioned above in the menu card")
                    continue
                ice_choice = input("Enter your ice cream size ( s/l ) : ")
                self.get_ice_cream.append(ice_flavour)
                if ice_choice == 's':
                    self.get_ice_cream_cost.append(4)
                elif ice_choice == 'l':
                    self.get_ice_cream_cost.append(8)
                else:
                    print("Please select the correct option")
                    continue
                choice = input("Do you need to add more ice creams in your order ( y/n ) : ")
                if choice == 'y':
                    continue
                else:
                    break

    def password(self):
        for i in range(0, 3):
            password = input("password please : ")
            if password == "deluxepizza":
                break
            else:
                if i == 2:
                    print("Sorry - you are not authorized to perform requested action")
                    self.__str__()
                continue

    def calcCost(self):
        if self.size == 's':
            pizzaCost = 10
        elif self.size == 'm':
            pizzaCost = 12
        elif self.size == 'l':
            pizzaCost = 14

        cheeseCost = self.cheese_toppings * 2
        pepperoniCost = self.pepperoni_toppings * 2
        mushroomCost = self.mushroom_toppings * 2
        veggieCost = self.veggie_toppings * 2

        totalCost = pizzaCost + cheeseCost + pepperoniCost + mushroomCost + veggieCost
        if self.discount == 'y':
            if self.disc_choice == 'y':
                totalCost += 5

        print(f"cost : ${totalCost}")
        self.get_cost.append(totalCost)

    def iceCost(self):
        totalCost = sum(self.get_cost) + sum(self.get_ice_cream_cost)
        if len(self.get_ice_cream_cost) == 0:
            pass
        else:
            print(f"Total amount with icecream(s) is ${totalCost}")

    def pizzasOfSize(self, details):
        print()
        if self.details not in self.get_size:
            print(f"There is no pizza order of size {self.details.upper()} in the list")

        elif self.details == 's':
            x = self.get_size.index('s')
            b = bool(self.get_cheese_dough[x])
            print(f"Pizza # {x + 1}")
            print(f"Pizza size : {self.details.upper()}")
            print(f"Cheese filled dough : {b}")
            print(f"Number of cheese toppings : {self.get_cheese_toppings[x]}")
            print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[x]}")
            print(f"Number of mushroom toppings : {self.get_mushroom_toppings[x]}")
            print(f"Number of veggie toppings : {self.get_veggie_toppings[x]}")
            if self.discount == 'y':
                if self.disc_choice == 'y':
                    print(f"Cost for ( pizza, cold drinks, french fries ) : ${self.get_cost[x]}")
                else:
                    print(f"Cost : ${self.get_cost[x]}")
            else:
                print(f"Cost : ${self.get_cost[x]}")

        elif self.details == 'm':
            x = self.get_size.index('m')
            b = bool(self.get_cheese_dough[x])
            print(f"Pizza # {x + 1}")
            print(f"Pizza size : {self.details.upper()}")
            print(f"Cheese filled dough : {b}")
            print(f"Number of cheese toppings : {self.get_cheese_toppings[x]}")
            print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[x]}")
            print(f"Number of mushroom toppings : {self.get_mushroom_toppings[x]}")
            print(f"Number of veggie toppings : {self.get_veggie_toppings[x]}")
            if self.discount == 'y':
                if self.disc_choice == 'y':
                    print(f"Cost for ( pizza, cold drinks, french fries ) : ${self.get_cost[x]}")
                else:
                    print(f"Cost : ${self.get_cost[x]}")
            else:
                print(f"Cost : ${self.get_cost[x]}")

        elif self.details == 'l':
            x = self.get_size.index('l')
            b = bool(self.get_cheese_dough[x])
            print(f"Pizza # {x + 1}")
            print(f"Pizza size : {self.details.upper()}")
            print(f"Cheese filled dough : {b}")
            print(f"Number of cheese toppings : {self.get_cheese_toppings[x]}")
            print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[x]}")
            print(f"Number of mushroom toppings : {self.get_mushroom_toppings[x]}")
            print(f"Number of veggie toppings : {self.get_veggie_toppings[x]}")
            if self.discount == 'y':
                if self.disc_choice == 'y':
                    print(f"Cost for ( pizza, cold drinks, french fries ) : ${self.get_cost[x]}")
                else:
                    print(f"Cost : ${self.get_cost[x]}")

            else:
                print(f"Cost : ${self.get_cost[x]}")

    def __str__(self):
        while True:
            print("\nPapa John, what do you want to do ?")
            print("\t1. Enter a new pizza order ( password required )")
            print("\t2. Change information of a specific order ( password required )")
            print("\t3. Display details for all pizzas of a specific size ( S/M/L )")
            print("\t4. Statistics on today's pizzas")
            print("\t5. Quit")
            choice = int(input("Please enter your choice > "))

            if choice == 1:
                self.password()
                while True:
                    a = len(todaysPizzas)
                    print("\nPlease refer the menu card below")
                    pizza_det = PrettyTable()
                    disc_det = PrettyTable()
                    pizza_columns = ["PIZZA", "COST ($)"]
                    pizza_det.add_column(pizza_columns[0], ["Small", "Medium", "Large", " "])
                    pizza_det.add_column(pizza_columns[1], ["10", "12", "14", "  "])

                    print(pizza_det)
                    self.discount = input("\nWanna know about discount !!! ( y/n ) : ")
                    if self.discount == 'y':
                        print("\nIf you order cold drinks and french fries seperately in the sense, it costs about")
                        print("Cold drinks  -> $5")
                        print("French fries -> $5")
                        print("Please choose the combo pack below\n")
                        disc_column = ["COMBO PACK", "COST ($)"]
                        disc_det.add_column(disc_column[0],
                                            ["Small with CD & FF", "Medium with CD & FF", "Large with CD & FF"])
                        disc_det.add_column(disc_column[1], ["15", "17", "19"])

                        print(disc_det)
                        self.disc_choice = input("\nDo you want to go with discount ( y/n ) : ")

                    pizza_count = int(input("\nHow many pizzas are in this order ? "))
                    if pizza_count > a:
                        print(f"Sorry I have less amount of ingrediants to make {a} numbers of pizza(s) only")
                        continue
                    else:
                        break

                for i in range(1, pizza_count + 1):
                    print(f"\nPizza number {i}")
                    self.getSize()
                    self.stuffedWithCheesed()
                    self.getCheese()
                    self.getPepperoni()
                    self.getMushroom()
                    self.getVeggie()
                    self.calcCost()
                    self.getIceCream(i)
                    self.iceCost()

            elif choice == 2:
                self.password()
                modify = input("\nWhich pizza do you wish to modify ? ")
                if modify not in self.get_size:
                    print(f"Sorry {modify.upper()} sized pizza is not in the order list")
                    print("Please check the order")
                    continue

                self.details = modify
                self.pizzasOfSize(self.details)
                ind = self.get_size.index(modify)
                while True:
                    print("\nJohn, what would you like to change ? ")
                    print("\t1. Size")
                    print("\t2. Cheese filled or not")
                    print("\t3. Number of cheese topppings")
                    print("\t4. Number of pepperoni topppings")
                    print("\t5. Number of mushroom topppings")
                    print("\t6. Number of veggie topppings")
                    print("\t7. Quit")
                    choice = int(input("Enter your choice > "))

                    if choice == 1:
                        self.getSize()
                        self.get_size.remove(modify)
                        self.get_size.insert(ind, self.size)

                    elif choice == 2:
                        self.stuffedWithCheesed()
                        if self.cheese_dough == 'y':
                            val = 1
                        elif self.cheese_dough == 'n':
                            val = 0
                        value = self.get_cheese_dough[ind]
                        self.get_cheese_dough.remove(value)
                        self.get_cheese_dough.insert(ind, val)

                    elif choice == 3:
                        self.getCheese()
                        value = self.get_cheese_toppings[ind]
                        self.get_cheese_toppings.remove(value)
                        self.get_cheese_toppings.insert(ind, self.cheese_toppings)

                    elif choice == 4:
                        self.getPepperoni()
                        value = self.get_pepperoni_toppings[ind]
                        self.get_pepperoni_toppings.remove(value)
                        self.get_pepperoni_toppings.insert(ind, self.pepperoni_toppings)

                    elif choice == 5:
                        self.getMushroom()
                        value = self.get_mushroom_toppings[ind]
                        self.get_mushroom_toppings.remove(value)
                        self.get_mushroom_toppings.insert(ind, self.mushroom_toppings)

                    elif choice == 6:
                        self.getVeggie()
                        value = self.get_veggie_toppings[ind]
                        self.get_veggie_toppings.remove(value)
                        self.get_veggie_toppings.insert(ind, self.veggie_toppings)

                    elif choice == 7:
                        break


            elif choice == 3:
                self.details = input("\nJohn, what size pizza do you want a list of ? ( s/m/l ) : ")
                self.pizzasOfSize(self.details)

            elif choice == 4:
                while True:
                    print("\nJohn, what information would you like ?")
                    print("\t1. Cost and details of cheapest pizza")
                    print("\t2. Cost and details of most costly pizza")
                    print("\t3. Number of pizzas sold today")
                    print("\t4. Number of pizzas of a specific size")
                    print("\t5. Average cost of pizzas")
                    print("\t6. Quit")
                    choice = int(input("Enter your choice > "))
                    if choice == 1:
                        highestPrice(self)

                    elif choice == 2:
                        lowestPrice(self)

                    elif choice == 3:
                        print(f"Number of pizzas sold today is {len(self.get_size)}")

                    elif choice == 4:
                        self.specific_size = input("\nWhat size pizza do you want ? ( s/m/l ) : ")
                        specific_size_count = self.get_size.count(self.specific_size)
                        print(f"Number of {self.specific_size.upper()} pizza(s) made today is {specific_size_count}")
                        self.details = self.specific_size
                        self.pizzasOfSize(self.details)

                    elif choice == 5:
                        avg = mean(self.get_cost)
                        print(f"Average cost of pizzas sold today is ${round(avg, 2)}")

                    elif choice == 6:
                        break

                    else:
                        print("Please select the correct option")


            elif choice == 5:
                print("\nHave a nice day")
                print(
                    "Please give feedback about our service, It would be more helpful for us to improve our "
                    "performance")
                feedback_choice = input("Do you like to give feedback ( y/n ) : ")
                if feedback_choice == 'y':
                    feedback = input("\nPlease give here : ")
                    print("Thank you for your valuable words")

                print("\nThanks for coming, Visit again !!!")
                exit()

            else:
                print("Please enter a correct option")

            continue


one = Pizza()
Deluxepizza = Pizza

print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\t   Welcome to Papa John's PIZZERIA")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
todaysPizzas = []

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour <= 11:
    greet = "good morning"
elif hour >= 12 and hour <= 17:
    greet = "good afternoon"
else:
    greet = "good evening"

a = int(input(f"\n{greet} ! How many pizzas can you make today ? "))
for j in range(1, a + 1):
    todaysPizzas.append(j)

print(one)
