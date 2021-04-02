# Hector wants to save money to go on a trip and puts some money in his bank account every day. He begins by putting
# $1 on Monday, and everyday from Tuesday to Sunday he will put in $1 more dollar than the day before. On every
# following Monday he will put in $1 more dollar than the previous Monday.
# Create a program that will take some value “n” and then return the total amount of money he will have in his bank
# account at the end of the nth day.


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
