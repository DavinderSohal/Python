# Print Patterns
# Placing one loop inside the body of another loop is called nesting. When you "nest" two loops, the outer loop takes
# control of the number of complete repetitions of the inner loop.
# Write the code that will generate the output as shown below:
#     -Ask the user, how many lines this triangle must contain. (1 to n lines)
#     -The display pattern must respect the pattern below.
#
# How the program should interact with the user: 
#
#               How many lines? 8
#
#               ***************
#                *************
#                 ***********
#                  *********
#                   *******
#                    *****
#                     ***
#                      *

no_of_lines = int(input("\nHow many lines? "))

print("")
for x in range(0, no_of_lines):
    for y in range(0, x):
        print(" ", end = "")
    for z in range(x, no_of_lines):
        print("*", end = "")
    for w in range(x, no_of_lines - 1):
        print("*", end = "")
    print("")
