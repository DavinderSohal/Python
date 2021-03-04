total = 0

present = 1

n = int(input("Enter number of days: "))

for i in range(1, n + 1):
    total = total + present

    if (i + 1) % 7 == 1:
        present = present - 5
    else:
        present = present + 1

print("Total Saving is:", total)
