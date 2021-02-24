"""
At LaRonde amusement park, there is some restrictions regarding the height of individuals to partake on certain rides
Create a program that asks the user for their height and receives the input using the input() function. The minimum
height for the ride is 120cm and someone lower than 130cm must be with an adult to go on the ride. Make the program
using branching statement and input function and display the appropriate print statements to the user.
Create a separate program that use if elif else statements and not nested if statements.
"""

height = input("Enter your height(in cms): ")
if int(height) < 120:
    print("You do not meet the height requirements(must be more than 120cm). You can't take this ride")
elif int(height) > 120 and int(height) < 130:
    print("To go on this ride, you must be with an adult.")
else:
    print("You can go for the ride. Thanku")
quit()
