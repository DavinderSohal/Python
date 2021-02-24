no_of_lines = int(input("How many lines this triangle must contain: "))

for x in range(0, no_of_lines):
    for y in range(0, x):
        print(" ", end = "")
    for z in range(x, no_of_lines):
        print("*", end = "")
    for w in range(x, no_of_lines-1):
        print("*", end = "")
    print("")
