# class DeluxePizza:
#     number_of_pizzas = 0
#
#     def __init__(self, size_of_pizza = "s", cheese_toppings = 0, pepperoni_toppings = 0, mushroom_toppings = 0,
#                  veggie_toppings = 0, stuffed_with_cheese = False):
#         self.size_of_pizza = size_of_pizza
#         self.cheese_toppings = cheese_toppings
#         self.pepperoni_toppings = pepperoni_toppings
#         self.mushroom_toppings = mushroom_toppings
#         self.veggie_toppings = veggie_toppings
#         self.stuffed_with_cheese = stuffed_with_cheese
#         DeluxePizza.number_of_pizzas += 1
#
#     def get_size_of_pizza(self):
#         """Accessor method of size of pizza attribute."""
#         if self.size_of_pizza.lower() == "s":
#             return "small"
#         elif self.size_of_pizza.lower() == "m":
#             return "medium"
#         else:
#             return "large"
#
#     def get_cheese_toppings(self):
#         """Accessor method of cheese toppings attribute."""
#         return self.cheese_toppings
#
#     def get_pepperoni_toppings(self):
#         """Accessor method of pepperoni toppings attribute."""
#         return self.pepperoni_toppings
#
#     def get_mushroom_toppings(self):
#         """Accessor method of mushroom toppings attribute."""
#         return self.mushroom_toppings
#
#     def get_veggie_toppings(self):
#         """Accessor method of veggie toppings attribute."""
#         return self.veggie_toppings
#
#     def get_stuffed_with_cheese(self):
#         """Accessor method of stuffed with cheese attribute."""
#         return self.stuffed_with_cheese
#
#     def get_number_of_pizzas(self):
#         """Accessor method of number of pizzas attribute."""
#         return self.number_of_pizzas
#
#     def set_size_of_pizza(self, size_of_pizza):
#         """Mutator method of size of pizza attribute."""
#         self.size_of_pizza = size_of_pizza
#
#     def set_cheese_toppings(self, cheese_toppings):
#         """Mutator method of cheese toppings attribute."""
#         self.cheese_toppings = cheese_toppings
#
#     def set_pepperoni_toppings(self, pepperoni_toppings):
#         """Mutator method of pepperoni toppings attribute."""
#         self.pepperoni_toppings = pepperoni_toppings
#
#     def set_mushroom_toppings(self, mushroom_toppings):
#         """Mutator method of mushroom toppings attribute."""
#         self.mushroom_toppings = mushroom_toppings
#
#     def set_veggie_toppings(self, veggie_toppings):
#         """Mutator method of veggie toppings attribute."""
#         self.veggie_toppings = veggie_toppings
#
#     def set_stuffed_with_cheese(self, stuffed_with_cheese):
#         """Mutator method of stuffed with cheese attribute."""
#         self.stuffed_with_cheese = stuffed_with_cheese
#
#     def calc_cost(self):
#         if not self.stuffed_with_cheese:
#             if self.size_of_pizza.lower() == "s":
#                 cost_of_pizza = 10 + (
#                         self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
#                                 self.veggie_toppings * 3
#             elif self.size_of_pizza.lower() == "m":
#                 cost_of_pizza = 12 + (
#                         self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
#                                 self.veggie_toppings * 3
#             else:
#                 cost_of_pizza = 14 + (
#                         self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
#                                 self.veggie_toppings * 3
#             return cost_of_pizza
#         else:
#             if self.size_of_pizza.lower() == "s":
#                 cost_of_pizza = 10 + (
#                         self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
#                                 self.veggie_toppings * 3 + 2
#             elif self.size_of_pizza.lower() == "m":
#                 cost_of_pizza = 12 + (
#                         self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
#                                 self.veggie_toppings * 3 + 4
#             else:
#                 cost_of_pizza = 14 + (
#                         self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
#                                 self.veggie_toppings * 3 + 6
#             return cost_of_pizza
#
#     def __str__(self):
#         return f"\nPizza # {self.get_number_of_pizzas()}" \
#                f"\n\tPizza size: {self.get_size_of_pizza()}" \
#                f"\n\tCheese filled dough: {self.stuffed_with_cheese}" \
#                f"\n\t# of cheese toppings: {self.cheese_toppings}" \
#                f"\n\t# of pepperoni toppings: {self.pepperoni_toppings}" \
#                f"\n\t# of mushroom toppings: {self.mushroom_toppings}" \
#                f"\n\t# of vegetable toppings: {self.veggie_toppings}" \
#                f"\n\tCost: ${self.calc_cost()}"
#
#
# def main():
#     my_pizza1 = DeluxePizza()
#     print(my_pizza1)
#     my_pizza2 = DeluxePizza("m", 1, 2, 3, 4)
#     print(my_pizza2)
#     my_pizza3 = DeluxePizza("l", 1, 2, 2, 3, True)
#     print(my_pizza3)
#
#
# if __name__ == '__main__':
#     main()


import datetime


def welcome():
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
    for i in range(3):
        password = input("Enter password: ")
        if password == "":
            break
        elif i == 2:
            print("\nSorry - you are not authorized to perform requested action")
            main()
        else:
            continue


def pizza_quantity():
    while True:
        pizza_count = int(input("\nHow many pizzas are in this order ? "))
        if pizza_count > today_pizza.count({}):
            print(
                f"Sorry I have less amount of ingredients to make {today_pizza.count({})} numbers of pizza(s) "
                f"only")
            continue
        else:
            return pizza_count


def cheaper_than(price):
    cheap_list = []
    for i in range(len(today_pizza) - today_pizza.count({})):
        if today_pizza[i]['cost'] <= price:
            cheap_list.append("Pizza # " + str(i + 1) + ", cost: $" + today_pizza[i]['cost'])
    return cheap_list


def lowest_price():
    cost_list = []
    for i in range(len(today_pizza) - today_pizza.count({})):
        cost_list.append(today_pizza[i]['cost'])
    if len(cost_list) == 0:
        return None
    else:
        index_cheapest = cost_list.index(min(cost_list))
        return index_cheapest


def highest_price():
    cost_list = []
    for i in range(len(today_pizza) - today_pizza.count({})):
        cost_list.append(today_pizza[i]['cost'])
    if len(cost_list) == 0:
        return None
    else:
        index_costly = cost_list.index(max(cost_list))
        return index_costly


def number_of_pizzas_of_size(size):
    number_of_pizzas_of_specific_size = 0
    for i in range(len(today_pizza) - today_pizza.count({})):
        if today_pizza[i]['size'] == size:
            number_of_pizzas_of_specific_size += 1
    return number_of_pizzas_of_specific_size


def average_cost():
    add = 0
    for i in range(len(today_pizza) - today_pizza.count({})):
        add += today_pizza[i]['cost']
    if add == 0:
        return None
    else:
        return add / (len(today_pizza) - today_pizza.count({}))


class DeluxePizza:
    number_of_pizzas = 0
    modify = 0

    def __init__(self, size_of_pizza = "s", cheese_toppings = 0, pepperoni_toppings = 0, mushroom_toppings = 0,
                 veggie_toppings = 0, stuffed_with_cheese = False):
        self.size_of_pizza = size_of_pizza
        self.cheese_toppings = cheese_toppings
        self.pepperoni_toppings = pepperoni_toppings
        self.mushroom_toppings = mushroom_toppings
        self.veggie_toppings = veggie_toppings
        self.stuffed_with_cheese = stuffed_with_cheese
        DeluxePizza.number_of_pizzas += 1

    def get_size_of_pizza(self):
        """Accessor method of size of pizza attribute."""
        return self.size_of_pizza

    def get_cheese_toppings(self):
        """Accessor method of cheese toppings attribute."""
        return self.cheese_toppings

    def get_pepperoni_toppings(self):
        """Accessor method of pepperoni toppings attribute."""
        return self.pepperoni_toppings

    def get_mushroom_toppings(self):
        """Accessor method of mushroom toppings attribute."""
        return self.mushroom_toppings

    def get_veggie_toppings(self):
        """Accessor method of veggie toppings attribute."""
        return self.veggie_toppings

    def get_stuffed_with_cheese(self):
        """Accessor method of stuffed with cheese attribute."""
        return self.stuffed_with_cheese

    def get_number_of_pizzas(self):
        """Accessor method of number of pizzas attribute."""
        return self.number_of_pizzas

    def set_size_of_pizza(self, size_of_pizza):
        """Mutator method of size of pizza attribute."""
        if size_of_pizza.lower() == "s" or size_of_pizza.lower() == "small":
            self.size_of_pizza = "small"
        elif size_of_pizza.lower() == "m" or size_of_pizza.lower() == "medium":
            self.size_of_pizza = "medium"
        else:
            self.size_of_pizza = "large"

    def set_cheese_toppings(self, cheese_toppings):
        """Mutator method of cheese toppings attribute."""
        self.cheese_toppings = cheese_toppings

    def set_pepperoni_toppings(self, pepperoni_toppings):
        """Mutator method of pepperoni toppings attribute."""
        self.pepperoni_toppings = pepperoni_toppings

    def set_mushroom_toppings(self, mushroom_toppings):
        """Mutator method of mushroom toppings attribute."""
        self.mushroom_toppings = mushroom_toppings

    def set_veggie_toppings(self, veggie_toppings):
        """Mutator method of veggie toppings attribute."""
        self.veggie_toppings = veggie_toppings

    def set_stuffed_with_cheese(self, stuffed_with_cheese):
        """Mutator method of stuffed with cheese attribute."""
        if stuffed_with_cheese == "y" or stuffed_with_cheese is True:
            self.stuffed_with_cheese = True
        else:
            self.stuffed_with_cheese = False

    def pizza_details(self):
        details = {'size': self.get_size_of_pizza(), 'stuffed': self.get_stuffed_with_cheese(),
                   'cheese': self.get_cheese_toppings(), 'pepperoni': self.get_pepperoni_toppings(),
                   'mushroom': self.get_mushroom_toppings(), 'veggie': self.get_veggie_toppings(),
                   'cost': self.calc_cost()}
        index = today_pizza.index({})
        today_pizza[index] = details

    def pizza_input(self, i):
        self.set_size_of_pizza(input(f"\nPizza # {i} size please (s/m/l): "))
        self.set_stuffed_with_cheese(input("Cheese in dough (y/any key for no)? "))
        self.set_cheese_toppings(int(input("Number of cheese toppings: ")))
        self.set_pepperoni_toppings(int(input("Number of pepperoni toppings: ")))
        self.set_mushroom_toppings(int(input("Number of Mushroom toppings: ")))
        self.set_veggie_toppings(int(input("Number of veggie toppings: ")))
        self.pizza_details()

    def modify_pizza(self):
        self.modify = int(input("\nWhich pizza do you wish to modify ? "))
        while self.modify > (len(today_pizza) - today_pizza.count({})) or self.modify <= 0:
            print(f"There is no pizza # {self.modify}"
                  f"\nThere are only {len(today_pizza) - today_pizza.count({})} pizza(s) in your order")
            option = input(
                "\n==> Press 1 to enter another pizza number or press anything else to quit this operation and go "
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
                    print("\nInvalid value!\nPlease choose again")

                self.set_size_of_pizza(today_pizza[self.modify - 1]['size'])
                self.set_stuffed_with_cheese(today_pizza[self.modify - 1]['stuffed'])
                self.set_cheese_toppings(today_pizza[self.modify - 1]['cheese'])
                self.set_pepperoni_toppings(today_pizza[self.modify - 1]['pepperoni'])
                self.set_mushroom_toppings(today_pizza[self.modify - 1]['mushroom'])
                self.set_veggie_toppings(today_pizza[self.modify - 1]['veggie'])
                today_pizza[self.modify - 1]['cost'] = self.calc_cost()

    def pizzas_of_size(self, size):
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
            print(f"\nThere is no pizza order of size {size.upper()} in the list")
        print("\n\t\t...............")
        print(f"\nNumber of pizzas of {size.upper()} size:", count)

    def pizzas_statistics(self):
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
                    print("\nThere is no pizza order in the list")
                else:
                    self.modify = index_cheapest + 1
                    print(f"\npizza # {self.modify} is the cheapest pizza")
                    print(self.__str__())
            elif stat == 2:
                index_costly = highest_price()
                if index_costly is None:
                    print("\nThere is no pizza order in the list")
                else:
                    self.modify = index_costly + 1
                    print(f"\npizza # {self.modify} is the most costly pizza")
                    print(self.__str__())
            elif stat == 3:
                print(
                    f"\nNumber of pizzas sold today({datetime.date.today()}): "
                    f"{len(today_pizza) - today_pizza.count({})}")
            elif stat == 4:
                specific_size = input("\nWhat size pizza do you want?(s/m/l): ")
                self.pizzas_of_size(specific_size)
            elif stat == 5:
                avg = average_cost()
                if avg is None:
                    print("\nThere is no pizza order in the list")
                else:
                    print(f"\nAverage cost of pizzas sold today({datetime.date.today()}): ${round(avg, 2)}")
            elif stat == 6:
                break
            else:
                print("\n------ Invalid value! choose again ------")

    def calc_cost(self):
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
        return f"\tPizza size: {today_pizza[self.modify - 1]['size']}" \
               f"\n\tCheese filled dough: {today_pizza[self.modify - 1]['stuffed']}" \
               f"\n\t# of cheese toppings: {today_pizza[self.modify - 1]['cheese']}" \
               f"\n\t# of pepperoni toppings: {today_pizza[self.modify - 1]['pepperoni']}" \
               f"\n\t# of mushroom toppings: {today_pizza[self.modify - 1]['mushroom']}" \
               f"\n\t# of vegetable toppings: {today_pizza[self.modify - 1]['veggie']}" \
               f"\n\tCost: ${today_pizza[self.modify - 1]['cost']}"


def main():
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
            p_quantity = pizza_quantity()
            for i in range(1, p_quantity + 1):
                my_pizza = DeluxePizza()
                my_pizza.pizza_input(i)
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
            print("\nAnother days work done!!!\nThank you and have a nice day!\n\t\t＼( ･_･)")
            exit()


if __name__ == '__main__':
    today_pizza = welcome()
    main()
