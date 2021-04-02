choice = "yes"
while choice == "yes":
    value = int(input("Enter the value: "))
    while value < 4 or value > 10:
        print("Invalid value! please try again")
        value = int(input("Enter the value: "))
    for i in range(1, value + 1, 2):
        for j in range(value - 1, i - 1, -1):
            print(end = " ")
        num = 1
        for k in range(1, i + 1):
            print(str(num), end = " ")
            num = num + 1
        print()
    if value % 2 == 0:
        for i in range(value - 1, 0, -2):
            for j in range(value - 1, i - 1, -1):
                print(end = " ")
            num = 1
            for k in range(1, i + 1):
                print(num, end = " ")
                num = num + 1
            print()
    else:
        for i in range(value - 2, 0, -2):
            for j in range(value - 1, i - 1, -1):
                print("", end = " ")
            num = 1
            for k in range(1, i + 1):
                print(num, end = " ")
                num = num + 1
            print()
    choice = input("Display another pattern: (yes/no): ")
    print("Thank u")

