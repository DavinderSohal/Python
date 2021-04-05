class MyClass:
    def first(self, first_arg):
        self.first_arg = first_arg
        return self.first_arg

    def second(self, second_arg):
        self.second_arg = second_arg
        return self.second_arg


x = MyClass()

x.first('1st')
x.second('2nd')

mydict = x.__dict__
print(mydict)
