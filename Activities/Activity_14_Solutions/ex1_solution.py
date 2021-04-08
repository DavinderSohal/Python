
class Person:
    def __init__ (self, name, ramq, address):  
        self.name = name
        self.ramq = ramq  
        self.address = address

class Student(Person):
    def __init__ (self, name, ramq, address, courses, grades, enrollment):  
        Person.__init__(self, name, ramq, address) # Base class constructor  
        self.courses = courses
        self.grades = grades  
        self.enrollment = enrollment

albert = Student(name="Albert Einstein", ramq="14031879-1235",  address="112 Mercer Street, Princeton",  courses=["Physics", "Relativity"],  grades=["B","A"], enrollment=1895)

