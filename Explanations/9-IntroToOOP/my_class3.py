

class Person:
    """Set name attribute"""     
    def set_name(self, name):
        self.name = name        
    """Return name attribute """
    def get_name(self):
        return self.name     
        
p1 = Person()
p2 = Person()
p2.set_name("Lucas")
p1.set_name("Jane Doe")

print(p1.get_name())
print(p1.name)

    