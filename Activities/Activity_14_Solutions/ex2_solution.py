
#Exercise 2 Solution

class Person:
    def __init__ (self, name, ramq, address):  
        self.name = name
        self.ramq = ramq  
        self.address = address

class Student(Person):
    def __init__ (self, name, ramq, address = None, courses = None, grades = None, enrollment = None):  
        Person.__init__(self, name, ramq, address) # Base class constructor  
        self.courses = courses
        self.grades = grades  
        self.enrollment = enrollment


class StudentGroup:# ... constructor and add_student() methods omitted 
    def __init__(self, students=[]):
        self.students = students
    def add_student(self, student):
        self.students.append(student)
    def get_names(self): #Return list of names of students in group 
        names = []
        for student in self.students:  
            names.append(student.name)
        return names

# Create student objects
albert = Student(name="Albert Einstein", ramq="19940379-1235")  
niels = Student(name="Niels Bohr", ramq="00188885-7459")

# Create student group object
group = StudentGroup(students=[albert, niels])

# Call get_names method  
print(group.get_names())
