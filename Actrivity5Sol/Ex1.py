# Activity 5 Solutions
# Exericse 1

# Create a tuple called triple of size 3 containing the  numbers 1, 2, and 3

triple = (1, 2, 3)

# Create three variables x, y and z and use the tuple triplet to initialize them.

x, y, z = triple

# Now create a tuple called quad of size 4, and try it again. What happens?

quad = (1, 2, 3, 4)
# x,y,z = quad This part is commented out as it would result in an error!


x, y, z = quad[:3]  # Only use index 0,1,2

print(x)
print(y)
print(z)
