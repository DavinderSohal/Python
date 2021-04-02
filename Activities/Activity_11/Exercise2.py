class person:
    def print_person(self, name, age):
        self.name = name
        self.age = age


p1 = person()
p1.print_person("Davinder", 23)
print(p1.name + " " + str(p1.age))
