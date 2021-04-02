# At LaRonde amusement park, there is some restrictions regarding the height of individuals to partake on certain rides
# Create a program that asks the user for their height and receives the input using the input() function. The minimum
# height for the ride is 120cm and someone lower than 130cm must be with an adult to go on the ride. Make the program
# using branching statement and input function and display the appropriate print statements to the user.
# Create a separate program that use if elif else statements and not nested if statements.

print("WELCOME TO THE AMUSEMENT PARK")
print("SOME OF THE RIDES HAVE THE RESTRICTIONS SO, PLEASE FILL YOUR INFORMATION")
i = input("Enter the height of yours in cm: ")
if 120 < int(i) < 130:
    print("You must an adult with you to go on this ride")
elif int(i) > 130:
    print("You are eligible for this ride alone.ENJOY...")
else:
    print("SORRY.You are not eligible for this ride")
quit()
