# Hector wants to save money to go on a trip and puts some money in his bank account every day. He begins by putting
# $1 on Monday, and everyday from Tuesday to Sunday he will put in $1 more dollar than the day before. On every
# following Monday he will put in $1 more dollar than the previous Monday.
# Create a program that will take some value “n” and then return the total amount of money he will have in his bank
# account at the end of the nth day.

n = int(input("Enter value of n: "))

total = 0
count = 1
monday = 1

for val in range(n):
    total = total + count

    if (val + 1) % 7 != 0:
        count = count + 1
    else:
        monday = monday + 1
        count = monday

print("Total money: ", total)
