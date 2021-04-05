# Using your solution from any activity (such Activity 4 or Activity 6) modify your code to create a file and log all
# of the output when running the program to a text file.
# Your code should log all of the print statements of your program until the user has quit the application.
# A new file log could be created for each instance of the run

print("Name: {first_name} {last_name} \nAge: {age}".format(
    first_name = "Davinder",
    last_name = "Sohal",
    age = 24))

with open("exrc2.txt", 'w') as f:
    f.write("Name: {first_name} {last_name} \nAge: {age}\n".format(
        first_name = "Davinder",
        last_name = "Sohal",
        age = 24))
    f.write("My second Line\n")
