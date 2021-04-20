

a = 1        #place a into the name space 
def f():     #When f called, a new namespace is created
    a = 2    #Insert a into a temp namespace of the function
    print(a) #Looking for a in the current name space, a = 2 

print(f())   #a inside the function refers to 2
print(a)     #a outside the function refers to 1



