# Write a class called Person with a constructor that takes two arguments, name and age and the saves these as
# attributes
# Write a method in this called print_person that prints out this information the console
# Confirm that you did it properly by instantiating an object called p1 and calling the method on the object.
# Lastly, extend the constructor by adding functionality that checks the input name only contains letters (no numbers
# allowed).

class person:
    def print_person(self, name, age):
        self.name = name
        self.age = age


p1 = person()
p1.print_person("Davinder", 23)
print(p1.name + " " + str(p1.age))
