# Exercise 2 - The code is incomplete, add your classes from exercise one and add a get_names method

class Person:
    def __init__(self, name = "Albert Einstein", ramq = "14031879-1235", address = "112 Mercer Street, Princeton"):
        self.name = name
        self.ramq = ramq
        self.address = address


class Student():
    def __init__(self, name = "Albert Einstein", ramq = "14031879-1235", address = "112 Mercer Street, Princeton",
                 courses = ["Physics", "Relativity"], grades = ["A", "A"], enrollment = 1895):
        Person.__init__(self, name, ramq, address)  # Base class constructor
        self.name = name
        self.ramq = ramq
        self.address = address
        self.courses = courses
        self.grades = grades
        self.enrollment = enrollment


class StudentGroup():
    def __init__(self, students = []):
        '''Constructor. The list of students'''
        self.students = students
        '''Constructor add a new student to the group'''

    def add_student(self, student):
        self.students.append(student)

    def get_name(self):
        for i in self.students:
            print(self.students)


niels = Student(name = "Niels Bohr", ramq = "07101885-7459",
                address = "Carlsberg Aresbolig, Gamle Carlsbergvej, Valby",
                courses = [],
                grades = [],
                enrollment = 1903)

albert = Student(name = "Albert Einstein", ramq = "14079-1235")

dream_team = StudentGroup([albert, niels])

dream_team.add_student(albert)
dream_team.get_name()
