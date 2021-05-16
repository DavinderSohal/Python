# -----------------------------------------------------
# Assignment # 2, Papa John PIZZERIA
# Written by: Davinder Singh (2092836), Navneet Kaur (2092453) and Simranjit Kaur (2092430)
# This program helps Papa John, the owner of Papa Johns Pizzeria, in keeping track of the number and types of pizzas
# he has cooked on a given day and to produce statistics regarding the choices her customers made.
# -----------------------------------------------------

import datetime  # module to get date and time

from prettytable import PrettyTable  # module to create a table


def welcome():
    """
    This will print the welcome message
    Take input from user on how many pizza they can make and return an empty list of same size

    Variable today_pizzas: will keep track of pizzas
    :return: list today_pizzas
    """
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\t   Welcome to Papa John's PIZZERIA")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        greet = "Good morning"
    elif 12 <= hour <= 17:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    maximum_pizzas = int(input(f"\n{greet}! How many pizzas can you make today ? "))
    today_pizzas = [{}] * maximum_pizzas
    return today_pizzas


def password_check():
    """
    This function will check if the password entered is correct
    :return: None
    """
    for i in range(3):
        password = input("Enter password: ")
        if password == "deluxepizza":
            break
        elif i == 2:
            print("\n\t---- Sorry - you are not authorized to perform requested action ----")
            main()
        else:
            continue


def pizza_quantity(name, ordered):
    """
    This function will ask user about the number of pizzas of specific name they want to order and return that value
    :param name: String name of the pizza ordered
    :param ordered: int number of pizzas already ordered
    :return: int pizza_count
    """
    while True:
        pizza_count = int(input(f"How many {name} pizzas are in this order ? "))
        # entered value should not exceed the limit of pizzas they can make today
        if pizza_count > today_pizza.count({}) - ordered:
            print(
                f"\n\t---- Sorry I can only make {today_pizza.count({}) - ordered} numbers of pizza(s) at this moment "
                f"----\n")
            continue
        else:
            return pizza_count


def pizzas_list(pizza):
    """
    This function will display the menu to the user to select their items from it and then return the number of
    orders made and the name of item
    :param pizza: list list of names of pizzas ordered so far
    :return: int ordered, list pizza_name
    """

    # table1 and table2 are objects to create tables
    table1 = PrettyTable()
    table2 = PrettyTable()
    table1.field_names = ["", "ITEM", "SMALL", "MEDIUM", "LARGE"]
    table1.add_rows([
        ["1.", "Pacific Veggie", "$10", "$12", "$14"],
        ["2.", "Fiery Hawaiian", "$10", "$12", "$14"],
        ["3.", "Cheeseburger Feast", "$10", "$12", "$14"],
        ["4.", "Deluxe Feast", "$10", "$12", "$14"],
        ["5.", "ExtravaganZZa Feast", "$10", "$12", "$14"],
        ["", "", "", "", ""],
        ["", "Regular dough", "$0", "$0", "$0"],
        ["", "Cheese stuffed dough", "$2", "$4", "$6"]
        ])
    print("\n\t\t\t------------ MENU ------------ ")
    print(table1)
    table2.add_column("TOPPINGS", ["Cheese", "Pepperoni", "Mushroom", "Veggies"])
    table2.add_column("PRICE", [2, 2, 2, 3])
    print(table2)
    name_list = ["Pacific Veggie", "Fiery Hawaiian", "Cheeseburger Feast", "Deluxe Feast", "ExtravaganZZa Feast"]
    ordered = 0
    pizza_name = pizza
    while True:
        if today_pizza.count({}) == 0:
            print("\n\t---- Sorry! I don't have ingredients to make any more pizzas ----")
            break
        else:
            p_number = int(
                input("\nWhich pizza you want to order from menu above?(enter the number only) OR Press 0 to quit "))
            if p_number not in range(6):
                print("------- Please choose the pizza which is mentioned above in the menu card ------")
                continue
            if p_number == 0:
                break
            count = pizza_quantity(name_list[p_number - 1], ordered)  # making call to function pizza_quantity
            ordered += count
            for i in range(count):
                pizza_name.append(name_list[p_number - 1])
            want_continue = input("\nWant to order another pizza?(y/n) ")
            if want_continue.lower() == "y":
                if (ordered + len(today_pizza) - today_pizza.count({})) == len(today_pizza):
                    print("\n\t---- Sorry! I don't have ingredients to make any more pizzas ----")
                    break
                else:
                    continue
            else:
                break
    return ordered, pizza_name


def combo_offer():
    """
    This function will show the user available combo deals and ask them to choose one from them
    :return: dict combo_details  dictionary containing the name and cost of combo offer selected
    """
    combo_table = PrettyTable()
    combo_table.add_column("", ["1.", "2.", "3.", "4."])
    combo_table.add_column("ITEM", ["Coke + Garlic Bread-sticks", "Canada dry + Garlic Bread-sticks",
                                    "Sprite + Garlic Bread-sticks", "Gold Peak + Garlic Bread-sticks"])
    combo_table.add_column("SMALL", ["$5", "$5", "$5", "$5"])
    combo_table.add_column("MEDIUM", ["$6", "$6", "$6", "$6"])
    combo_table.add_column("LARGE", ["$7", "$7", "$7", "$7"])
    print(combo_table)
    combo_item = ["Coke + Garlic Bread-sticks", "Canada dry + Garlic Bread-sticks", "Sprite + Garlic Bread-sticks",
                  "Gold Peak + Garlic Bread-sticks"]
    combo = int(input("\nWhich option you want?(enter the number only) OR Press 0 to quit "))
    while combo not in range(5):
        print("------- Please choose the offer which is mentioned above in the menu card ------")
        combo = int(input("\nWhich option you want?(enter the number only) "))
    if combo == 0:
        return {'name': "NA", 'cost': 0}
    combo_size = input("Select size(s/m/l): ")
    if combo_size.lower() == "s":
        cost = 5
    elif combo_size.lower() == "m":
        cost = 6
    else:
        cost = 7
    combo_details = {'name': combo_item[combo - 1], 'cost': cost}
    return combo_details


def dessert():
    """
    This function will display the available desserts and prompt the user for input
    :return: list dessert_name, int dessert_cost  names and cost of the desserts selected
    """
    dessert_table = PrettyTable()
    dessert_kind = input("What kind of dessert you want?(hot/cold) ")
    dessert_name = []
    dessert_cost = 0
    if dessert_kind.lower() == "hot":
        # for HOT desserts
        dessert_table.add_column("", ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8."])
        dessert_table.add_column("ITEM", ["Mango Pudding", "Coconut Pudding", "Chocolate Pudding", "Molten Lava Cakes",
                                          "Coconut Flour Brownies", "Apple Pie Tacos", "Chai Mug Cake",
                                          "Cinnamon Bun Palmier"])
        dessert_table.add_column("PRICE", ["$7", "$7", "$7", "$10", "$10", "$10", "$10", "$10"])
        print(dessert_table)
        dessert_item = ["Mango Pudding", "Coconut Pudding", "Chocolate Pudding", "Molten Lava Cakes",
                        "Coconut Flour Brownies", "Apple Pie Tacos", "Chai Mug Cake", "Cinnamon Bun Palmier"]
        while True:
            select_dessert = int(input("\nWhich item you want?(enter the number only) OR Press 0 to quit "))
            if select_dessert not in range(9):
                print("------- Please choose the item which is mentioned above in the menu card ------")
                continue
            if select_dessert == 0:
                break
            dessert_name.append(dessert_item[select_dessert - 1])
            if 1 <= select_dessert <= 3:
                dessert_cost += 7
            else:
                dessert_cost += 10
            want_continue = input("\nWant to order another dessert?(y/n) ")
            if want_continue.lower() == "y":
                continue
            else:
                break
    else:
        # for COLD desserts
        dessert_table.add_column("", ["1.", "2."])
        dessert_table.add_column("ITEM", ["Ice Cream", "Frozen yogurt"])
        dessert_table.add_column("PRICE", ["$7", "$8"])
        print(dessert_table)
        dessert_item = ["Ice Cream", "Frozen yogurt"]
        while True:
            select_dessert = int(input("\nWhich item you want?(enter the number only) OR Press 0 to quit "))
            if select_dessert not in range(3):
                print("------- Please choose the item which is mentioned above in the menu card ------")
                continue
            if select_dessert == 0:
                break
            dessert_name.append(dessert_item[select_dessert - 1])
            if select_dessert == 1:
                dessert_cost += 7
            else:
                dessert_cost += 8
            want_continue = input("\nWant to order another dessert?(y/n) ")
            if want_continue.lower() == "y":
                continue
            else:
                break
    return dessert_name, dessert_cost


def cheaper_than(price):
    """
    This function will return list of all the pizzas that are cheaper than the price entered by user
    :param price: int  price value user entered
    :return: list cheap_list
    """
    cheap_list = []
    for i in range(len(today_pizza) - today_pizza.count({})):
        if today_pizza[i]['cost'] <= price:
            cheap_list.append("Pizza # " + str(i + 1) + ", cost: $" + today_pizza[i]['cost'])
    return cheap_list


def lowest_price():
    """
    This function will go through the list of ordered pizzas and return the index of cheapest pizza among them
    :return: int index_cheapest
    """
    # creating a list of cost of all the ordered pizzas
    cost_list = []
    for i in range(len(today_pizza) - today_pizza.count({})):
        cost_list.append(today_pizza[i]['cost'])
    if len(cost_list) == 0:
        return None
    else:
        index_cheapest = cost_list.index(min(cost_list))
        return index_cheapest


def highest_price():
    """
    This function will go through the list of ordered pizzas and return the index of most expensive pizza among them
    :return: int index_costly
    """
    # creating a list of cost of all the ordered pizzas
    cost_list = []
    for i in range(len(today_pizza) - today_pizza.count({})):
        cost_list.append(today_pizza[i]['cost'])
    if len(cost_list) == 0:
        return None
    else:
        index_costly = cost_list.index(max(cost_list))
        return index_costly


def number_of_pizzas_of_size(size):
    """
    This function will return the number of pizza of the size needed
    :param size: String size of the pizza
    :return: int number_of_pizzas_of_specific_size
    """
    number_of_pizzas_of_specific_size = 0
    for i in range(len(today_pizza) - today_pizza.count({})):
        if today_pizza[i]['size'] == size:
            number_of_pizzas_of_specific_size += 1
    return number_of_pizzas_of_specific_size


def average_cost():
    """
    This function will return the average cost of all the pizzas ordered
    :return: average cost of pizzas
    """
    add = 0
    for i in range(len(today_pizza) - today_pizza.count({})):
        add += today_pizza[i]['cost']
    if add == 0:
        return None
    else:
        return add / (len(today_pizza) - today_pizza.count({}))


class DeluxePizza:
    """
    A class DeluxePizza to handle to details about pizza
    ...
    Class Attributes
    ----------------
    number_of_pizzas: String  store the value of how many times class object is called
    modify: int  store the value of pizza number user want to manage

    Class instances
    ---------------
    size_of_pizza: String  size of the pizza
    cheese_toppings: int  number of cheese toppings added
    pepperoni_toppings: int  number of pepperoni toppings added
    mushroom_toppings: int  number of mushroom toppings added
    veggie_toppings: int  number of veggie toppings added
    stuffed_with_cheese: bool  dough stuffed with cheese or not
    """
    number_of_pizzas = 0
    modify = 0

    def __init__(self, size_of_pizza = "s", cheese_toppings = 0, pepperoni_toppings = 0, mushroom_toppings = 0,
                 veggie_toppings = 0, stuffed_with_cheese = False):
        """
        created a constructor to initialize the class instance variables
        :param size_of_pizza: String, optional   size of pizza ordered (default is s)
        :param cheese_toppings: int, optional  number of cheese toppings added (default is 0)
        :param pepperoni_toppings: int, optional  number of pepperoni toppings added (default is 0)
        :param mushroom_toppings: int, optional  number of mushroom toppings added (default is 0)
        :param veggie_toppings: int, optional  number of veggie toppings added (default is 0)
        :param stuffed_with_cheese: bool, optional  dough stuffed with cheese or not (default is False)
        """
        self.size_of_pizza = size_of_pizza
        self.cheese_toppings = cheese_toppings
        self.pepperoni_toppings = pepperoni_toppings
        self.mushroom_toppings = mushroom_toppings
        self.veggie_toppings = veggie_toppings
        self.stuffed_with_cheese = stuffed_with_cheese
        DeluxePizza.number_of_pizzas += 1

    def get_size_of_pizza(self):
        """
        Accessor method of size of pizza attribute.
        :return: String size_of_pizza
        """
        return self.size_of_pizza

    def get_cheese_toppings(self):
        """
        Accessor method of cheese toppings attribute.
        :return: int cheese_toppings
        """
        return self.cheese_toppings

    def get_pepperoni_toppings(self):
        """
        Accessor method of pepperoni toppings attribute.
        :return: int pepperoni_toppings
        """
        return self.pepperoni_toppings

    def get_mushroom_toppings(self):
        """
        Accessor method of mushroom toppings attribute.
        :return: int mushroom_toppings
        """
        return self.mushroom_toppings

    def get_veggie_toppings(self):
        """
        Accessor method of veggie toppings attribute.
        :return: int veggie_toppings
        """
        return self.veggie_toppings

    def get_stuffed_with_cheese(self):
        """
        Accessor method of stuffed with cheese attribute.
        :return: bool stuffed_with_cheese
        """
        return self.stuffed_with_cheese

    def get_number_of_pizzas(self):
        """
        Accessor method of number of pizzas attribute.
        :return: int number_of_pizzas
        """
        return self.number_of_pizzas

    def set_size_of_pizza(self, size_of_pizza):
        """
        Mutator method of size of pizza attribute.
        :param size_of_pizza: String  size of pizza entered by user
        """
        if size_of_pizza.lower() == "s" or size_of_pizza.lower() == "small":
            self.size_of_pizza = "small"
        elif size_of_pizza.lower() == "m" or size_of_pizza.lower() == "medium":
            self.size_of_pizza = "medium"
        else:
            self.size_of_pizza = "large"

    def set_cheese_toppings(self, cheese_toppings):
        """
        Mutator method of cheese toppings attribute.
        :param cheese_toppings: int number of cheese toppings
        """
        self.cheese_toppings = cheese_toppings

    def set_pepperoni_toppings(self, pepperoni_toppings):
        """
        Mutator method of pepperoni toppings attribute.
        :param pepperoni_toppings: int number of pepperoni toppings
        """
        self.pepperoni_toppings = pepperoni_toppings

    def set_mushroom_toppings(self, mushroom_toppings):
        """
        Mutator method of mushroom toppings attribute.
        :param mushroom_toppings: int number of mushroom toppings
        """
        self.mushroom_toppings = mushroom_toppings

    def set_veggie_toppings(self, veggie_toppings):
        """
        Mutator method of veggie toppings attribute.
        :param veggie_toppings: int number of veggie toppings
        """
        self.veggie_toppings = veggie_toppings

    def set_stuffed_with_cheese(self, stuffed_with_cheese):
        """
        Mutator method of stuffed with cheese attribute.
        :param stuffed_with_cheese: bool dough stuffed with cheese or not
        """
        """"""
        if stuffed_with_cheese == "y" or stuffed_with_cheese is True:
            self.stuffed_with_cheese = True
        else:
            self.stuffed_with_cheese = False

    def pizza_details(self, p_name):
        """
        This method will store the details of pizza ordered in a dictionary and append that in a nested list
        :param p_name: list  names of pizzas ordered
        """
        index = today_pizza.index({})
        details = {'size': self.get_size_of_pizza(), 'name': p_name[index],
                   'stuffed': self.get_stuffed_with_cheese(), 'cheese': self.get_cheese_toppings(),
                   'pepperoni': self.get_pepperoni_toppings(), 'mushroom': self.get_mushroom_toppings(),
                   'veggie': self.get_veggie_toppings(), 'cost': self.calc_cost()}
        today_pizza[index] = details

    def pizza_input(self, i, p_name):
        """
        This method will take input from user about the pizza attributes.
        :param i: int  index of the pizza
        :param p_name: list  names of pizzas ordered
        """
        self.set_size_of_pizza(input(f"\nPizza # {i} size please (s/m/l): "))
        self.set_stuffed_with_cheese(input("Cheese in dough (y/any key for no)? "))
        self.set_cheese_toppings(int(input("Number of cheese toppings: ")))
        self.set_pepperoni_toppings(int(input("Number of pepperoni toppings: ")))
        self.set_mushroom_toppings(int(input("Number of Mushroom toppings: ")))
        self.set_veggie_toppings(int(input("Number of veggie toppings: ")))
        self.pizza_details(p_name)

    def modify_pizza(self):
        """
        This method will ask about the pizza number they want to modify and then will provide them with options to
        make changes.
        """
        self.modify = int(input("\nWhich pizza do you wish to modify ? "))
        while self.modify > (len(today_pizza) - today_pizza.count({})) or self.modify <= 0:
            print(f"There is no pizza # {self.modify}"
                  f"\nThere are only {len(today_pizza) - today_pizza.count({})} pizza(s) in your order")
            option = input(
                "\n\t==> Press 1 to enter another pizza number or press anything else to quit this operation and go "
                "back to main menu\n")
            if option == "1":
                self.modify = int(input("\nWhich pizza do you wish to modify ? "))
            else:
                break
        else:
            print("\nPizza #", self.modify)
            print(self.__str__())

            while True:
                choice = int(input("\nPapa John, what would you like to change?"
                                   "\n\t1. Size"
                                   "\n\t2. Cheese filled or not"
                                   "\n\t3. Number of cheese toppings"
                                   "\n\t4. Number of pepperoni toppings"
                                   "\n\t5. Number of mushroom toppings"
                                   "\n\t6. Number of vegetable toppings"
                                   "\n\t7. Quit"
                                   "\n\tEnter choice > "))
                if choice == 1:
                    self.set_size_of_pizza(input("\nsize please (s/m/l): "))
                    today_pizza[self.modify - 1]['size'] = self.get_size_of_pizza()
                elif choice == 2:
                    self.set_stuffed_with_cheese(input("\nCheese in dough (y/any key for no)? "))
                    today_pizza[self.modify - 1]['stuffed'] = self.get_stuffed_with_cheese()
                elif choice == 3:
                    today_pizza[self.modify - 1]['cheese'] = int(input("\nNumber of cheese toppings: "))
                elif choice == 4:
                    today_pizza[self.modify - 1]['pepperoni'] = int(input("\nNumber of pepperoni toppings: "))
                elif choice == 5:
                    today_pizza[self.modify - 1]['mushroom'] = int(input("\nNumber of Mushroom toppings: "))
                elif choice == 6:
                    today_pizza[self.modify - 1]['veggie'] = int(input("\nNumber of veggie toppings: "))
                elif choice == 7:
                    break
                else:
                    print("\n\t---- Invalid value! ----\n\t     Please choose again")

                self.set_size_of_pizza(today_pizza[self.modify - 1]['size'])
                self.set_stuffed_with_cheese(today_pizza[self.modify - 1]['stuffed'])
                self.set_cheese_toppings(today_pizza[self.modify - 1]['cheese'])
                self.set_pepperoni_toppings(today_pizza[self.modify - 1]['pepperoni'])
                self.set_mushroom_toppings(today_pizza[self.modify - 1]['mushroom'])
                self.set_veggie_toppings(today_pizza[self.modify - 1]['veggie'])
                today_pizza[self.modify - 1]['cost'] = self.calc_cost()

    def pizzas_of_size(self, size):
        """
        This function will take size from parameter and will display the details of pizzas of that specific size
        :param size: String  size of which we want the list of pizzas
        """
        if size == "s":
            size = "small"
        elif size == "m":
            size = "medium"
        else:
            size = "large"
        count = 0
        print(f"\nList of pizzas of size {size.upper()} sold today:")
        for i in range(len(today_pizza) - today_pizza.count({})):
            if today_pizza[i]['size'] == size:
                self.modify = i + 1
                print("\nPizza #", self.modify)
                print(self.__str__())
                count += 1
        if count == 0:
            print(f"\n\tThere is no pizza order of size {size.upper()} in the list")
        print("\n\t\t...............")
        print(f"\nNumber of pizzas of {size.upper()} size:", count)

    def pizzas_statistics(self):
        """
        This method will provide user with many option which will display information about the pizzas ordered.
        """
        while True:
            stat = int(input("\nPapa John, what information would you like?"
                             "\n\t1. Cost and details of cheapest pizza"
                             "\n\t2. Cost and details of most costly pizza"
                             "\n\t3. Number of pizzas sold today"
                             "\n\t4. Number of pizzas of a specific size"
                             "\n\t5. Average cost of pizzas"
                             "\n\t6. Quit"
                             "\nEnter your choice > "))
            if stat == 1:
                index_cheapest = lowest_price()
                if index_cheapest is None:
                    print("\n---- There is no pizza order in the list ----")
                else:
                    self.modify = index_cheapest + 1
                    print(f"\npizza # {self.modify} is the cheapest pizza")
                    print(self.__str__())
            elif stat == 2:
                index_costly = highest_price()
                if index_costly is None:
                    print("\n\t---- There is no pizza order in the list ----")
                else:
                    self.modify = index_costly + 1
                    print(f"\npizza # {self.modify} is the most costly pizza")
                    print(self.__str__())
            elif stat == 3:
                print(
                    f"\n\tNumber of pizzas sold today({datetime.date.today()}): "
                    f"{len(today_pizza) - today_pizza.count({})}")
            elif stat == 4:
                specific_size = input("\nWhat size pizza do you want?(s/m/l): ")
                self.pizzas_of_size(specific_size)
            elif stat == 5:
                avg = average_cost()
                if avg is None:
                    print("\n\t---- There is no pizza order in the list ----")
                else:
                    print(f"\n\tAverage cost of pizzas sold today({datetime.date.today()}): ${round(avg, 2)}")
            elif stat == 6:
                break
            else:
                print("\n------ Invalid value! choose again ------")

    def calc_cost(self):
        """
        This method will calculate the cost of order made, i.e., cost of pizza (s/m/l) + cost of toppings + cost of
        crust
        :return: int cost_of_pizza
        """
        if not self.get_stuffed_with_cheese():
            if self.get_size_of_pizza() == "small":
                cost_of_pizza = 10 + (
                        self.get_cheese_toppings() + self.get_pepperoni_toppings() + self.get_mushroom_toppings()) * \
                                2 + self.get_veggie_toppings() * 3
            elif self.get_size_of_pizza() == "medium":
                cost_of_pizza = 12 + (
                        self.get_cheese_toppings() + self.get_pepperoni_toppings() + self.get_mushroom_toppings()) * \
                                2 + self.get_veggie_toppings() * 3
            else:
                cost_of_pizza = 14 + (
                        self.get_cheese_toppings() + self.get_pepperoni_toppings() + self.get_mushroom_toppings()) * \
                                2 + self.get_veggie_toppings() * 3
            return cost_of_pizza
        else:
            if self.get_size_of_pizza() == "small":
                cost_of_pizza = 10 + (
                        self.get_cheese_toppings() + self.get_pepperoni_toppings() + self.get_mushroom_toppings()) * \
                                2 + self.get_veggie_toppings() * 3 + 2
            elif self.get_size_of_pizza() == "medium":
                cost_of_pizza = 12 + (
                        self.get_cheese_toppings() + self.get_pepperoni_toppings() + self.get_mushroom_toppings()) * \
                                2 + self.get_veggie_toppings() * 3 + 4
            else:
                cost_of_pizza = 14 + (
                        self.get_cheese_toppings() + self.get_pepperoni_toppings() + self.get_mushroom_toppings()) * \
                                2 + self.get_veggie_toppings() * 3 + 6
            return cost_of_pizza

    def __str__(self):
        """
        This method will print the information of the pizza
        :return: all information about pizza
        """
        return f"\tPizza size: {today_pizza[self.modify - 1]['size']}" \
               f"\n\tPizza name: {today_pizza[self.modify - 1]['name']}" \
               f"\n\tCheese filled dough: {today_pizza[self.modify - 1]['stuffed']}" \
               f"\n\t# of cheese toppings: {today_pizza[self.modify - 1]['cheese']}" \
               f"\n\t# of pepperoni toppings: {today_pizza[self.modify - 1]['pepperoni']}" \
               f"\n\t# of mushroom toppings: {today_pizza[self.modify - 1]['mushroom']}" \
               f"\n\t# of vegetable toppings: {today_pizza[self.modify - 1]['veggie']}" \
               f"\n\tCost: ${today_pizza[self.modify - 1]['cost']}"


def main():
    pizzas_name = []
    d_name = []
    combo_info = {'name': "NA", 'cost': 0}
    d_cost = 0
    while True:
        print("\nPapa John, what do you want to do?"
              "\n\t1. Enter a new pizza order (password required)"
              "\n\t2. Change information of a specific order (password required)"
              "\n\t3. Display details for all pizzas of a specific size (s/m/l)"
              "\n\t4. Statistics on today’s pizzas"
              "\n\t5. Quit")
        choice = int(input("Please enter your choice > "))
        if choice < 1 or choice > 5:
            print("\n----- Please choose between 1 and 5 only (inclusive) -----")
            continue
        if choice == 1:
            password_check()
            p_quantity, p_name = pizzas_list(pizzas_name)
            for i in range(1, p_quantity + 1):
                my_pizza = DeluxePizza()
                my_pizza.pizza_input(i, pizzas_name)
            if not p_quantity == 0:
                see_combo = input("\nWant to see combo offers?(y/n) ")
                if see_combo.lower() == "y":
                    combo_info = combo_offer()
                else:
                    combo_info = {'name': "NA", 'cost': 0}
                want_dessert = input("\nWe also provide dessert, want to add in your order?(y/n) ")
                if want_dessert.lower() == "y":
                    d_name, d_cost = dessert()
                else:
                    pass
        elif choice == 2:
            password_check()
            my_pizza = DeluxePizza()
            my_pizza.modify_pizza()
        elif choice == 3:
            my_pizza = DeluxePizza()
            size_list = input("\nJohn, what size pizza do you want a list of ? (s/m/l): ")
            my_pizza.pizzas_of_size(size_list)
        elif choice == 4:
            my_pizza = DeluxePizza()
            my_pizza.pizzas_statistics()
        else:
            pizzas_name_set = list(set(pizzas_name))
            print("\nOrder Summary:")
            print(f"\tTotal pizzas ordered: {len(today_pizza) - today_pizza.count({})}")
            for item in pizzas_name_set:
                print(f"\t# of {item} pizzas: {pizzas_name.count(item)}")
            print(f"\tCombo pack: {combo_info['name']}")
            for item in range(len(d_name)):
                print(f"\tDessert # {item + 1}: {d_name[item]}")
            add = 0
            for i in range(len(today_pizza) - today_pizza.count({})):
                add += today_pizza[i]['cost']
            total_cost = add + combo_info['cost'] + d_cost
            print(f"Total cost of the order: ${total_cost}")
            print("\nAnother days work done!!!\nThank you and have a nice day!\n\t\t＼( ･_･)")
            exit()


if __name__ == '__main__':
    today_pizza = welcome()
    main()
