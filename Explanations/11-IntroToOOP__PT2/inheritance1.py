

class FirstClass():
    def first_function(self):
        print("This is the first function")
        

class SecondClass(FirstClass):
    def second_function(self):
        print("This is the second function")
        
        
        
s = SecondClass()
s.second_function()
s.first_function()
print("Welcome to Papa Johns")