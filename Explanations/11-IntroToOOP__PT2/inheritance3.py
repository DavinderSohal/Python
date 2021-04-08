

class Person:
    numberOfPeople = 0
    def __init__(self, name, ramq, address):  
        self.name = name
        self.ramq = ramq  
        self.address = address

class Student(Person):
    def __init__(self, name, ramq, address, courses, grades, enrollment):  
        self.courses = courses
        self.grades = grades  
        self.enrollment = enrollment
        
# What about the name, ramq and address parameters?

albert = Student(name="Albert Einstein", ramq="14031879-1235",  
                 address="112 Mercer Street, Princeton",
                 courses=["Relativity", "Physics"],  
                 grades=["B","A"], enrollment=1895)





