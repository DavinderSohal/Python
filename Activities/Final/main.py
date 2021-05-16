import datetime
from statistics import mean


def highestPrice(self):
    cheapest_pizza = min(self.get_cost)
    cheapest_pizza_index = self.get_cost.index(cheapest_pizza)
    b = bool(self.get_cheese_dough[cheapest_pizza_index])
    print(f"\nPizza # {cheapest_pizza_index + 1} is the cheapest pizza")
    print(f"Pizza size : {self.get_size[cheapest_pizza_index].upper()}")
    print(f"Cheese filled dough :{b}")
    print(f"Number of cheese toppings : {self.get_cheese_toppings[cheapest_pizza_index]}")
    print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[cheapest_pizza_index]}")
    print(f"Number of mushroom toppings : {self.get_mushroom_toppings[cheapest_pizza_index]}")
    print(f"Number of veggie toppings : {self.get_veggie_toppings[cheapest_pizza_index]}")
    print(f"Cost : ${self.get_cost[cheapest_pizza_index]}")
    self.__str__()


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
    self.__str__()


class Pizza:
    def __init__(self):
        self.get_size = []
        self.get_cheese_dough = []
        self.get_cheese_toppings = []
        self.get_pepperoni_toppings = []
        self.get_mushroom_toppings = []
        self.get_veggie_toppings = []
        self.get_cost = []

    def getSize(self):
        self.size = input("size ( s/m/l ) : ")
        self.get_size.append(self.size)
        return self.size

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
        return self.cheese_toppings

    def getPepperoni(self):
        self.pepperoni_toppings = int(input("number of pepperoni toppings : "))
        self.get_pepperoni_toppings.append(self.pepperoni_toppings)
        return self.pepperoni_toppings

    def getMushroom(self):
        self.mushroom_toppings = int(input("number of mushroom toppings : "))
        self.get_mushroom_toppings.append(self.mushroom_toppings)
        return self.mushroom_toppings

    def getVeggie(self):
        self.veggie_toppings = int(input("number of veggie toppings : "))
        self.get_veggie_toppings.append(self.veggie_toppings)
        return self.veggie_toppings

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
        self.get_cost.append(totalCost)
        print(f"cost : &{totalCost}")

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
