'''Class representing sequences of Person class''''''Constructor'''


class Person:
    '''Constructor'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    '''Print the sequence'''

    def print_person(self):
        print("%s\n%s" % (self.name, self.age))


p1 = Person("John", "55")
p1.print_person()
