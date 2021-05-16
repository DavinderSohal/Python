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
        if password == "deluxepizza":
            break
        elif i == 2:
            print("Sorry - you are not authorized to perform requested action")
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


def cheaper_than():
    if today_pizza['price':] < today_pizza['price':]:
        print(today_pizza)


class DeluxePizza:
    number_of_pizzas = 0

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
        if self.size_of_pizza.lower() == "s":
            self.size_of_pizza = "small"
        elif self.size_of_pizza.lower() == "m":
            self.size_of_pizza = "medium"
        else:
            self.size_of_pizza = "large"
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
        if self.stuffed_with_cheese == "y":
            self.stuffed_with_cheese = True
        else:
            self.stuffed_with_cheese = False
        return self.stuffed_with_cheese

    def get_number_of_pizzas(self):
        """Accessor method of number of pizzas attribute."""
        return self.number_of_pizzas

    def set_size_of_pizza(self, size_of_pizza):
        """Mutator method of size of pizza attribute."""
        self.size_of_pizza = size_of_pizza

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
        self.stuffed_with_cheese = stuffed_with_cheese.lower()

    def beverages(self):
        combo = input("Do you want your pizza with a combo : ")
        if combo == "yes":
            print("For beverages /n"
                  "1. Coke/n"
                  "2. Canada dry/n"
                  "3. Sprite/n"
                  "4. Gold Peak/n")
            drinks = input("What kind of cold drink do you want :")
            print(self.calc_cost() + 5)
        if combo == "no":
            drink = input("Do you want any drink : ")
            if drink == "yes":
                print("For beverages \n"
                      "1. Coke\n"
                      "2. Canada dry\n"
                      "3. Sprite\n"
                      "4. Gold Peak")
                print(self.calc_cost() + 4)
            else:
                print("ok")

    def pizza_details(self):
        details = {'size': self.get_size_of_pizza(), 'stuffed': self.get_stuffed_with_cheese(),
                   'cheese': self.get_cheese_toppings(), 'pepperoni': self.get_pepperoni_toppings(),
                   'mushroom': self.get_mushroom_toppings(), 'veggie': self.get_veggie_toppings(),
                   'price': self.calc_cost()}
        index = today_pizza.index({})
        today_pizza[index] = details
        print(today_pizza)

    def pizza_input(self, i):
        self.set_size_of_pizza(input(f"Pizza # {i} size please (s/m/l  ): "))
        self.set_stuffed_with_cheese(input("Cheese in dough (y/any key for no)? "))
        self.set_cheese_toppings(int(input("Number of cheese toppings: ")))
        self.set_pepperoni_toppings(int(input("Number of pepperoni toppings: ")))
        self.set_mushroom_toppings(int(input("Number of Mushroom toppings: ")))
        self.set_veggie_toppings(int(input("Number of veggie toppings: ")))
        self.beverages()
        self.pizza_details()

        # index = today_pizza.index(0)
        # if index == 0:
        #     today_pizza[index] = 1
        # else:
        #     today_pizza[index] = today_pizza[index - 1] + 1
        # print(today_pizza)

    def calc_cost(self):
        if not self.stuffed_with_cheese:
            if self.size_of_pizza.lower() == "s":
                cost_of_pizza = 10 + (
                        self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
                                self.veggie_toppings * 3
            elif self.size_of_pizza.lower() == "m":
                cost_of_pizza = 12 + (
                        self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
                                self.veggie_toppings * 3
            else:
                cost_of_pizza = 14 + (
                        self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
                                self.veggie_toppings * 3
            return cost_of_pizza
        else:
            if self.size_of_pizza.lower() == "s":
                cost_of_pizza = 10 + (
                        self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
                                self.veggie_toppings * 3 + 2
            elif self.size_of_pizza.lower() == "m":
                cost_of_pizza = 12 + (
                        self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
                                self.veggie_toppings * 3 + 4
            else:
                cost_of_pizza = 14 + (
                        self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings) * 2 + \
                                self.veggie_toppings * 3 + 6
            return cost_of_pizza

    def __str__(self):
        return f"\nPizza # {self.get_number_of_pizzas()}" \
               f"\n\tPizza size: {self.get_size_of_pizza()}" \
               f"\n\tCheese filled dough: {self.stuffed_with_cheese}" \
               f"\n\t# of cheese toppings: {self.cheese_toppings}" \
               f"\n\t# of pepperoni toppings: {self.pepperoni_toppings}" \
               f"\n\t# of mushroom toppings: {self.mushroom_toppings}" \
               f"\n\t# of vegetable toppings: {self.veggie_toppings}" \
               f"\n\tCost: ${self.calc_cost()}"


def main():
    while True:
        print("\nPapa John, what do you want to do?"
              "\n\t1. Enter a new pizza order (password required)"
              "\n\t2. Change information of a specific order (password required)"
              "\n\t3. Display details for all pizzas of a specific size (s/m/l)"
              "\n\t4. Statistics on today’s pizzas"
              "\n\t5. Desserts"
              "\n\t6. Quit")
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
                print(my_pizza)
        if choice == 5:
            desserts = input("What kind of dessert you want hot/cold")
            if desserts == "hot":
                print("IN HOT\n"
                      "1. Mango Pudding\n"
                      "2. Coconut Pudding"
                      "3. Chocolate Pudding\n"
                      "4. Molten Lava Cakes\n"
                      "5. Coconut Flour Brownies\n"
                      "6. Apple Pie Tacos\n"
                      "7. Chai Mug Cake\n"
                      "8. Cinnamon Bun Palmier")
                options = int(input("Whats your choice : "))
                if options >= 1 or options <= 3:
                    print("The amount is 7 dollars")
                elif options >= 4 or options <= 8:
                    print("The amount is 10 dollars")
                else:
                    print("We don't have that dessert")
            else:
                print("IN COLD\n"
                      "1. Ice cream\n"
                      "2. Frozen yogurt")
                cold = input("Whats your choice: ")
                print("The amount is 8 dollars")

        if choice == 6:
            exit()


if __name__ == '__main__':
    today_pizza = welcome()
    main()
