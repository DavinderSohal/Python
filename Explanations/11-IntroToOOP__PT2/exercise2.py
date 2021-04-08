#Exercise 2 - The code is incomplete, add your classes from exercise one and add a get_names method

class StudentGroup: 
    def __init__ (self, students=[]):
        '''Constructor. The list of students'''
        self.students = students
        '''Constructor add a new student to the group'''
    def add_student(self, student):
        self.students.append(student) 
    
#Create missing classes for in-class exercise    
    
albert = Student(name="Albert Einstein",ramq="14031879-1235",
                 address="112 Mercer Street, Princeton",  
                 courses=["Physics", "Relativity"],  
                 grades=["A","A"],
                 enrollment=1895)  

niels = Student(name="Niels Bohr", ramq="07101885-7459",
                address="Carlsberg Aresbolig, Gamle Carlsbergvej, Valby",  
                courses=[], 
                grades=[],  
                enrollment=1903)

albert = Student(name="Albert Einstein", ramq="14079-1235")


dream_team = StudentGroup([albert, niels])




