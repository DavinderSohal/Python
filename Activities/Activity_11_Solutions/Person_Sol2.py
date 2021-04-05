import re


class Person:
    def __init__(self, name, age):  # Save name as attribute
        self.name = name
        pattern = re.compile('[^A-Za-z]')
        if pattern.search(name):
            print("Error: Person contains illegal characters")
            # Save sequence as attribute  
        self.name = name.upper()
        '''Print the sequence'''


p1 = Person("John", "44")
