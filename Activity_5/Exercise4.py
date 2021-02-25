# Calculate Average
# Create the a python program that will generate the output as shown aside
# Let’s create a list of marks for a  student
# The program needs to ask how many marks the user can enter
# Take the input, then display each mark again and show the average of the student
# How the program should interact with the user     
#
#           How many marks for this student? 3
#           Mark 1: 75
#           Mark 2: 80
#           Mark 3: 75
#
#           The marks are 75, 80, 75,
#           The average is: 76.67%

number_of_marks = input("How many marks for this student? ")
mark = []
i = 1
while i <= int(number_of_marks):
    mark.append(input(f"Mark {i}: "))
    i += 1

summation = 0
print("\nThe marks are ", end = "")
for val in mark:
    print(val, end = ", ")
    summation += int(val)

print("\nThe average is: %(average)s%%" % {"average": round(summation / int(number_of_marks), 2)})
