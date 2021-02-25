# lists and loops
# Create the following list of numbers: [3,7,5,2,9,7]
# Write a while loop that will print out the numbers
# Write a for loop that will print out the numbers
# Using a loop, write the code that will print out all elements that are larger than their neighbor i.e.: (7,9)
# Write the code that will loop through the list and for every odd number prints: “Odd” and every even number “Even”

my_list = [3, 7, 5, 2, 9, 7]

i = 0
list_length = len(my_list)
print("Using while")
while i < list_length:
    print(my_list[i])
    i += 1

print("\nUsing for")
for val in my_list:
    print(val)

print("\nelements that are larger than their neighbor:")
x = 0
while x < list_length:
    if my_list[x] > my_list[x - 1] and my_list[x] > my_list[x + 1]:
        print(my_list[x])
    x += 1

print("\nODD and EVEN")
for val in my_list:
    if val % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
