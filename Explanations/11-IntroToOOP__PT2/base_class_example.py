

class A:
    def __init__ (self):  
        print("Initializing A")


class B(A):	# inherits from A  
    def init(self):
        A.__init__ (self)	#Call constructor of base class  
        print("Initializing B")

b = B()
#b.init()


