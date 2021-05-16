# all modules are build-in modules only, no need to download

import datetime  # module to find the time
from statistics import mean  # module to find the mean value

from prettytable import PrettyTable  # module to draw the tabular column


# method to fetch the lowest price of pizza ordered
def lowestPrice(self):
    cheapest_pizza = min(self.get_cost)  # fetch the minimum value in the get_cost list
    cheapest_pizza_index = self.get_cost.index(cheapest_pizza)  # find the index of the cheapest pizza in the list
    b = bool(self.get_cheese_dough[cheapest_pizza_index])  # boolean value for cheese dough ( True/False ) 

    # details of the cheapest pizza 
    print(f"\nPizza # {cheapest_pizza_index + 1} is the cheapest pizza")
    print(f"Pizza size : {self.get_size[cheapest_pizza_index].upper()}")
    print(f"Cheese filled dough : {b}")
    print(f"Number of cheese toppings : {self.get_cheese_toppings[cheapest_pizza_index]}")
    print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[cheapest_pizza_index]}")
    print(f"Number of mushroom toppings : {self.get_mushroom_toppings[cheapest_pizza_index]}")
    print(f"Number of veggie toppings : {self.get_veggie_toppings[cheapest_pizza_index]}")
    print(f"Cost : ${self.get_cost[cheapest_pizza_index]}")


# method to fetch the highest price of pizza ordered
def highestPrice(self):
    costly_pizza = max(self.get_cost)  # fetch the maximum value in the get_cost list
    costly_pizza_index = self.get_cost.index(costly_pizza)  # find the index of the costliest pizza in the list
    b = bool(self.get_cheese_dough[costly_pizza_index])  # boolean value for cheese dough ( True/False )

    # details of the costliest pizza  
    print(f"\nPizza # {costly_pizza_index + 1} is the most costliest pizza")
    print(f"Pizza size : {self.get_size[costly_pizza_index].upper()}")
    print(f"Cheese filled dough : {b}")
    print(f"Number of cheese toppings : {self.get_cheese_toppings[costly_pizza_index]}")
    print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[costly_pizza_index]}")
    print(f"Number of mushroom toppings : {self.get_mushroom_toppings[costly_pizza_index]}")
    print(f"Number of veggie toppings : {self.get_veggie_toppings[costly_pizza_index]}")
    print(f"Cost : ${self.get_cost[costly_pizza_index]}")


# class
class Pizza:
    # constructor
    def __init__(self):
        self.get_size = []  # list used to store & get the size of the pizza 
        self.get_cheese_dough = []  # list used to store & get the cheese dough 
        self.get_cheese_toppings = []  # list used to store & get the cheese toppings
        self.get_pepperoni_toppings = []  # list used to store & get the pepperoni toppings
        self.get_mushroom_toppings = []  # list used to store & get the mushroom toppings
        self.get_veggie_toppings = []  # list used to store & get the vegetable toppings
        self.get_ice_cream_cost = []  # list used to store & get the ice cream cost
        self.get_ice_cream = []  # list used to store & get the ice cream flavours
        self.get_cost = []  # list used to store & get the total cost of the pizza

    # method to get the size of the pizza from the user
    def setSize(self):
        while True:
            self.size = input("size ( s/m/l ) : ")
            if self.size == 's' or self.size == 'm' or self.size == 'l':
                break
            else:
                print("\nRead the menu card properly")
                continue
        self.get_size.append(self.size)  # will append the size in the get_size list 

    # method to get the cheese dough 
    def stuffedWithCheesed(self):
        while True:
            self.cheese_dough = input("cheese in dough ( y/n ) : ")
            if self.cheese_dough == 'y':
                self.get_cheese_dough.append(1)  # 1 represents True ( bool value )
                break
            elif self.cheese_dough == 'n':
                self.get_cheese_dough.append(0)  # 0 represents False ( bool value )
                break
            else:
                print("Please select the correct option")
                continue

    # method to get the number of cheese toppings 
    def setCheese(self):
        self.cheese_toppings = int(input("number of cheese toppings : "))
        self.get_cheese_toppings.append(self.cheese_toppings)  # will append the count in the get_cheese_toppings list

    # method to get the number of pepperoni toppings
    def setPepperoni(self):
        self.pepperoni_toppings = int(input("number of pepperoni toppings : "))
        self.get_pepperoni_toppings.append(
            self.pepperoni_toppings)  # will append the count in the get_pepperoni_toppings list

    # method to get the number of mushroom topping
    def setMushroom(self):
        self.mushroom_toppings = int(input("number of mushroom toppings : "))
        self.get_mushroom_toppings.append(
            self.mushroom_toppings)  # will append the count in the get_mushroom_toppings list

    # method to get the number of vegetable topping
    def setVeggie(self):
        self.veggie_toppings = int(input("number of veggie toppings : "))
        self.get_veggie_toppings.append(self.veggie_toppings)  # will append the count in the get_veggie_toppings list

    # method to get the ice cream flavour
    def setIceCream(self):
        print("\nWe have Ice creams too, If you like then just check that also")
        self.ice = input("Press 'y' to check the ice cream menu card : ")
        if self.ice == 'y':
            ice_cream_det = PrettyTable()  # Table creation object for ice cream menu card

            # Ice cream menu card details
            ice_columns = ["ICE CREAM", "Cost ($) small-cup", "Cost ($) large-cup"]
            ice_cream_det.add_column(ice_columns[0], ["Chocolate", "Strawberry", "Mix fruit", "Vennila"])
            ice_cream_det.add_column(ice_columns[1], ["4", "4", "4", "4"])
            ice_cream_det.add_column(ice_columns[2], ["8", "8", "8", "8"])

            print(ice_cream_det)  # will print the menu card ( tabular column )
            ice_avail_list = ["chocolate", "strawberry", "mix fruit",
                              "vennila"]  # user should choose the flavour from this list only
            while True:
                ice_flavour = input("Choose your flavour : ")  # ice cream flavour
                if ice_flavour.lower() not in ice_avail_list:  # incase user flavour is not there in the list,
                    # then the below block will run
                    print("Please choose the flavour which are mentioned above in the menu card")
                    continue
                ice_choice = input("Enter your ice cream size ( s/l ) : ")  # size of the ice cream
                self.get_ice_cream.append(ice_flavour)
                if ice_choice == 's':
                    self.get_ice_cream_cost.append(
                        4)  # cost of small size ice cream, will append the cost into get_ice_cream_cost list
                elif ice_choice == 'l':
                    self.get_ice_cream_cost.append(
                        8)  # cost of large size ice cream, will append the cost into get_ice_cream_cost list
                else:
                    print("Please select the correct option")
                    continue
                choice = input(
                    "Do you need to add more ice creams in your order ( y/n ) : ")  # for multiple ice cream order
                if choice == 'y':
                    continue
                else:
                    break

    # method for password handler                
    def password(self):
        for i in range(0, 3):  # user have 3 chance to type the correct password
            password = input("password please : ")
            if password == "deluxepizza":  # password
                break
            else:
                if i == 2:  # if the user fails to type the correct password, then the below block will run
                    print("Sorry - you are not authorized to perform requested action")
                    self.__str__()
                continue

    # method to find the total cost 
    def calcCost(self):
        if self.size == 's':
            pizzaCost = 10  # cost of small size pizza 
        elif self.size == 'm':
            pizzaCost = 12  # cost of medium size pizza 
        elif self.size == 'l':
            pizzaCost = 14  # cost of large size pizza 

        # $2 for each topping
        cheeseCost = self.cheese_toppings * 2
        pepperoniCost = self.pepperoni_toppings * 2
        mushroomCost = self.mushroom_toppings * 2
        veggieCost = self.veggie_toppings * 2

        # add the above all details 
        totalCost = pizzaCost + cheeseCost + pepperoniCost + mushroomCost + veggieCost
        if self.discount == 'y':
            if self.disc_choice == 'y':  # if the user select the combo offer pack
                totalCost += 5  # $5 will be added to the total cost ( for cold drinks & french fries )

        print(f"cost : ${totalCost}")  # print the cost of the pizza
        self.get_cost.append(totalCost)  # append the cost in the get_cost list

    # method to find the total cost with ice cream
    def iceCost(self):
        self.bill = sum(self.get_cost) + sum(
            self.get_ice_cream_cost)  # will add all values in the get_cost list and get_ice_cream_cost list
        if len(self.get_ice_cream_cost) == 0:
            pass
        else:
            print(f"Total amount with icecream(s) is ${self.bill}")  # print the ice cream cost

    # method to print the details of the pizza using size 
    def pizzasOfSize(self, details):
        print()
        if self.details not in self.get_size:  # will search the size in the get_size list, if it is not there,
            # then the below block will run
            print(f"There is no pizza order of size {self.details.upper()} in the list")

        elif self.details == 's':
            x = self.get_size.index('s')  # index of s
            b = bool(self.get_cheese_dough[x])  # boolean value for cheese dough ( True/False )

            # print the details of SMALL size pizza
            print(f"Pizza # {x + 1}")
            print(f"Pizza size : {self.details.upper()}")
            print(f"Cheese filled dough : {b}")
            print(f"Number of cheese toppings : {self.get_cheese_toppings[x]}")
            print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[x]}")
            print(f"Number of mushroom toppings : {self.get_mushroom_toppings[x]}")
            print(f"Number of veggie toppings : {self.get_veggie_toppings[x]}")
            if self.discount == 'y':
                if self.disc_choice == 'y':  # if the user select the discount offer, then the below block will run
                    print(f"Cost for ( pizza, cold drinks, french fries ) : ${self.get_cost[x]}")
                # if the user didn't select the discount offer, then it'll print the cost simply
                else:
                    print(f"Cost : ${self.get_cost[x]}")
            else:
                print(f"Cost : ${self.get_cost[x]}")

        elif self.details == 'm':
            x = self.get_size.index('m')  # index of m
            b = bool(self.get_cheese_dough[x])  # boolean value for cheese dough ( True/False )

            # print the details of MEDIUM size pizza
            print(f"Pizza # {x + 1}")
            print(f"Pizza size : {self.details.upper()}")
            print(f"Cheese filled dough : {b}")
            print(f"Number of cheese toppings : {self.get_cheese_toppings[x]}")
            print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[x]}")
            print(f"Number of mushroom toppings : {self.get_mushroom_toppings[x]}")
            print(f"Number of veggie toppings : {self.get_veggie_toppings[x]}")
            if self.discount == 'y':
                if self.disc_choice == 'y':  # if the user select the discount offer, then the below block will run
                    print(f"Cost for ( pizza, cold drinks, french fries ) : ${self.get_cost[x]}")

                # if the user didn't select the discount offer, then it'll print the cost simply
                else:
                    print(f"Cost : ${self.get_cost[x]}")
            else:
                print(f"Cost : ${self.get_cost[x]}")

        elif self.details == 'l':
            x = self.get_size.index('l')  # index of l
            b = bool(self.get_cheese_dough[x])  # boolean value for cheese dough ( True/False )

            # print the details of LARGE size pizza
            print(f"Pizza # {x + 1}")
            print(f"Pizza size : {self.details.upper()}")
            print(f"Cheese filled dough : {b}")
            print(f"Number of cheese toppings : {self.get_cheese_toppings[x]}")
            print(f"Number of pepperoni toppings : {self.get_pepperoni_toppings[x]}")
            print(f"Number of mushroom toppings : {self.get_mushroom_toppings[x]}")
            print(f"Number of veggie toppings : {self.get_veggie_toppings[x]}")
            if self.discount == 'y':
                if self.disc_choice == 'y':  # if the user select the discount offer, then the below block will run
                    print(f"Cost for ( pizza, cold drinks, french fries ) : ${self.get_cost[x]}")

                # if the user didn't select the discount offer, then it'll print the cost simply
                else:
                    print(f"Cost : ${self.get_cost[x]}")
            else:
                print(f"Cost : ${self.get_cost[x]}")

    def cost_value(self, details):
        if self.details == 's':
            self.value = 10
        elif self.details == 'm':
            self.value = 12
        elif self.details == 'l':
            self.value = 14

    # overwritting the __str__ method
    def __str__(self):
        while True:
            # options for user...
            print("\nPapa John, what do you want to do ?")
            print("\t1. Enter a new pizza order ( password required )")
            print("\t2. Change information of a specific order ( password required )")
            print("\t3. Display details for all pizzas of a specific size ( S/M/L )")
            print("\t4. Statistics on today's pizzas")
            print("\t5. Quit")
            choice = int(input("Please enter your choice > "))

            # pizza ordering section
            if choice == 1:
                self.password()  # check the password
                while True:
                    a = len(todaysPizzas)  # count of todaysPizzas list
                    print("\nPlease refer the menu card below")
                    pizza_det = PrettyTable()  # Table creation object for pizza menu card
                    disc_det = PrettyTable()  # Table creation object for discount details

                    # Pizza menu card details
                    pizza_columns = ["PIZZA", "COST ($)"]
                    pizza_det.add_column(pizza_columns[0], ["Small", "Medium", "Large", " "])
                    pizza_det.add_column(pizza_columns[1], ["10", "12", "14", "  "])

                    print(pizza_det)  # will print the pizza menu card

                    # Discount section
                    self.discount = input("\nWanna know about discount !!! ( y/n ) : ")
                    if self.discount == 'y':
                        print("\nIf you order cold drinks and french fries seperately in the sense, it costs about")
                        print("Cold drinks  -> $5")
                        print("French fries -> $5")
                        print("Please choose the combo pack below\n")

                        # Discount menu card details
                        disc_column = ["COMBO PACK", "COST ($)"]
                        disc_det.add_column(disc_column[0],
                                            ["Small with CD & FF", "Medium with CD & FF", "Large with CD & FF"])
                        disc_det.add_column(disc_column[1], ["15", "17", "19"])

                        print(disc_det)  # will print the discount menu card

                        self.disc_choice = input("\nDo you want to go with discount ( y/n ) : ")

                    pizza_count = int(input("\nHow many pizzas are in this order ? "))
                    if pizza_count > a:  # if the pizza_count greater than the todaysPizzas count, then the below
                        # block will run
                        print(f"Sorry I have less amount of ingrediants to make {a} numbers of pizza(s) only")
                        continue
                    else:
                        break

                # the below indent block will iterate till it reaches the user's order ( pizza_count )
                for i in range(1, pizza_count + 1):
                    print(f"\nPizza number {i}")
                    self.setSize()  # get the size
                    self.stuffedWithCheesed()  # get the cheese dough value 
                    self.setCheese()  # get the cheese toppings
                    self.setPepperoni()  # get the pepperoni toppings
                    self.setMushroom()  # get the mushroom toppings
                    self.setVeggie()  # get the veggie toppings
                    self.calcCost()  # return the total cost
                self.setIceCream()  # get the ice cream flavours
                self.iceCost()  # return the total cost & ice cream cost

            # changing pizza's information section
            elif choice == 2:
                self.password()  # check the password  
                print("\nYour orders : ", end = "")
                for piz in self.get_size:
                    print(f"{piz}", end = ", ")

                modify = input("\nWhich pizza do you wish to modify ? ")
                if modify not in self.get_size:  # if the pizza is not there, then the below block will run
                    print(f"Sorry {modify.upper()} sized pizza is not in the order list")
                    print("Please check the order")
                    continue

                self.details = modify
                self.pizzasOfSize(self.details)  # calling the method with the argument ( which should be modify )
                ind = self.get_size.index(modify)  # index of the pizza 

                while True:

                    # options for user...
                    print("\nJohn, what would you like to change ? ")
                    print("\t1. Size")
                    print("\t2. Cheese filled or not")
                    print("\t3. Number of cheese topppings")
                    print("\t4. Number of pepperoni topppings")
                    print("\t5. Number of mushroom topppings")
                    print("\t6. Number of veggie topppings")
                    print("\t7. Quit")
                    choice = int(input("\nEnter your choice > "))

                    # changing size
                    if choice == 1:
                        self.new_value = input("size to change : ")
                        if self.new_value == 's':
                            new_val = 10
                        elif self.new_value == 'm':
                            new_val = 12
                        elif self.new_value == 'l':
                            new_val = 14

                        self.get_size.remove(self.get_size[ind])
                        self.get_size.insert(ind, self.new_value)
                        val = self.get_cost[ind]
                        self.cost_value(self.details)
                        if self.value > val:
                            a = self.value - val
                        elif self.value < val:
                            a = val - self.value
                        b = a + new_val
                        self.get_cost.remove(self.get_cost[ind])
                        self.get_cost.insert(ind, b)

                    # changing cheese dough
                    elif choice == 2:
                        self.new_value = input("cheese dough to change : ")
                        if self.cheese_dough == 'y':
                            val = 1
                        elif self.cheese_dough == 'n':
                            val = 0
                        value = self.get_cheese_dough[ind]
                        self.get_cheese_dough.remove(value)
                        self.get_cheese_dough.insert(ind, val)

                    # changing number of cheese toppings
                    elif choice == 3:
                        self.new_value = int(input("number of cheese to change : "))
                        x = self.get_cheese_toppings[ind] * 2
                        self.get_cheese_toppings.remove(self.get_cheese_toppings[ind])
                        self.get_cheese_toppings.insert(ind, self.new_value)
                        if self.get_cost[ind] > x:
                            a = self.get_cost[ind] - x
                        elif self.get_cost[ind] < x:
                            a = x - self.get_cost[ind]
                        b = self.new_value * 2
                        c = a + b
                        self.get_cost.remove(self.get_cost[ind])
                        self.get_cost.insert(ind, c)

                        # changing number of pepperoni toppings
                    elif choice == 4:
                        self.new_value = int(input("number of pepperoni to change : "))
                        x = self.get_pepperoni_toppings[ind] * 2
                        self.get_pepperoni_toppings.remove(self.get_pepperoni_toppings[ind])
                        self.get_pepperoni_toppings.insert(ind, self.new_value)
                        if self.get_cost[ind] > x:
                            a = self.get_cost[ind] - x
                        elif self.get_cost[ind] < x:
                            a = x - self.get_cost[ind]
                        b = self.new_value * 2
                        c = a + b
                        self.get_cost.remove(self.get_cost[ind])
                        self.get_cost.insert(ind, c)

                        # changing number of mushroom toppings
                    elif choice == 5:
                        self.new_value = int(input("number of mushroom to change : "))
                        x = self.get_mushroom_toppings[ind] * 2
                        self.get_mushroom_toppings.remove(self.get_mushroom_toppings[ind])
                        self.get_mushroom_toppings.insert(ind, self.new_value)
                        if self.get_cost[ind] > x:
                            a = self.get_cost[ind] - x
                        elif self.get_cost[ind] < x:
                            a = x - self.get_cost[ind]
                        b = self.new_value * 2
                        c = a + b
                        self.get_cost.remove(self.get_cost[ind])
                        self.get_cost.insert(ind, c)

                        # changing number of vegetable toppings
                    elif choice == 6:
                        self.new_value = int(input("number of veggie to change : "))
                        x = self.get_veggie_toppings[ind] * 2
                        self.get_veggie_toppings.remove(self.get_veggie_toppings[ind])
                        self.get_veggie_toppings.insert(ind, self.new_value)
                        if self.get_cost[ind] > x:
                            a = self.get_cost[ind] - x
                        elif self.get_cost[ind] < x:
                            a = x - self.get_cost[ind]
                        b = self.new_value * 2
                        c = a + b
                        self.get_cost.remove(self.get_cost[ind])
                        self.get_cost.insert(ind, c)

                        # exit the info changing option
                    elif choice == 7:
                        break


            # printing details using size 
            elif choice == 3:
                self.details = input("\nJohn, what size pizza do you want a list of ? ( s/m/l ) : ")
                self.pizzasOfSize(self.details)


            # statistics 
            elif choice == 4:
                while True:
                    # options for user...
                    print("\nJohn, what information would you like ?")
                    print("\t1. Cost and details of cheapest pizza")
                    print("\t2. Cost and details of most costly pizza")
                    print("\t3. Number of pizzas sold today")
                    print("\t4. Number of pizzas of a specific size")
                    print("\t5. Average cost of pizzas")
                    print("\t6. Quit")
                    choice = int(input("Enter your choice > "))

                    # will return the cheapest pizza 
                    if choice == 1:
                        lowestPrice(self)

                    # will return the costliest pizza
                    elif choice == 2:
                        highestPrice(self)

                    # will return the total number pizza sold today
                    elif choice == 3:
                        print(f"Number of pizzas sold today is {len(self.get_size)}")

                    # will return the total number of speicific size pizza made today 
                    elif choice == 4:
                        self.specific_size = input("\nWhat size pizza do you want ? ( s/m/l ) : ")
                        specific_size_count = self.get_size.count(
                            self.specific_size)  # count the specific size in the get_size list
                        print(f"Number of {self.specific_size.upper()} pizza(s) made today is {specific_size_count}")
                        self.details = self.specific_size

                        # will print those pizza(s) details
                        self.pizzasOfSize(self.details)

                    # will return the average cost 
                    elif choice == 5:
                        avg = mean(self.get_cost)  # mean function helps to find the average
                        print(
                            f"Average cost of pizzas sold today is ${round(avg, 2)}")  # round function helps to
                        # round off the value into our desired count ( here 2)

                    # will break the loop and goes to main menu 
                    elif choice == 6:
                        break

                    # if the user's choice greater than 6, then the below block will run 
                    else:
                        print("Please select the correct option")


            # feedback section 
            elif choice == 5:
                # bill printing
                choice = input("Do you want to see the bill ( y/n ) : ")
                if choice == 'y':
                    print(f"Your bill : {self.bill}")
                else:
                    pass

                print("\nHave a nice day")

                # feedback section
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


one = Pizza()  # object for pizza class
Deluxepizza = Pizza  # renaming into Deluxepizza

# welcome message
print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\t   Welcome to Papa John's PIZZERIA")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

todaysPizzas = []  # number of pizzas will be there in this list

hour = int(datetime.datetime.now().hour)  # find the current time

# greetings according to the current time
if hour >= 0 and hour <= 11:
    greet = "good morning"
elif hour >= 12 and hour <= 17:
    greet = "good afternoon"
else:
    greet = "good evening"

a = int(input(f"\n{greet} ! How many pizzas can you make today ? "))  # total number of pizzas can made today
for j in range(1, a + 1):
    todaysPizzas.append(j)  # append the numbers in the todaysPizzas

print(one)
