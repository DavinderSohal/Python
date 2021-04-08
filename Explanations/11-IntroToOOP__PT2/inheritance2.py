x = 5 #global scope

def func():
    x = 10

class Person:
    pass
    # Attributes: name, cpr, address

class Employee(Person): # Inherits from Person
    pass  
    # Attributes: office

class Student(Person): # Inherits from Person 
    pass
    # Attributes: courses, grades, enrollment_data

class Technical(Employee): # Inherits from Employee
    pass   
    # Attributes: job_description

class Researcher(Employee): # Inherits from Employee
    pass

    # Attributes: research_interests, publications
    

