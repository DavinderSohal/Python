class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(self.name)
        print(self.age)


info = Person("navneet", 27)
info.print_person()
