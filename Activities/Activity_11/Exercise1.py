# Create an empty class called Car.
#
# Create a method called initialize in the class, which takes a name as input and saves it as a data attribute.
#
# Create an instance of the class, and save it in a variable called car.
#
# Call the initialize method with the string “Ford".

class Car:
    def initialize(self, name):
        self.data = name
        print(self.data)


car = Car()

car.initialize("ford")
