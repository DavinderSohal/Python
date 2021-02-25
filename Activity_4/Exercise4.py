# Write a complete application that inputs three integers from the user and displays the sum, average, product,
# smallest and largest of these numbers. The average calculation should result in a floating point number.
# For example, if the input is “1,2,3” the output should be:
#    Sum: 6
#    Average: 2
#    Product: 6
#    Smallest: 1
#    Largest: 3

integer1 = input("Enter 1st number: ")
integer2 = input("Enter 2nd number: ")
integer3 = input("Enter 3rd number: ")
Sum = int(integer1) + int(integer2) + int(integer3)
print("Sum: " + str(Sum))
Average = Sum / 3
print("Average : " + str(Average))
Product = int(integer1) * int(integer2) * int(integer3)
print("Product : " + str(Product))
if int(integer1) >= int(integer2) and int(integer1) >= int(integer3):
    print(str(integer1) + "is the largest number")
elif int(integer2) >= int(integer1) and int(integer2) >= int(integer3):
    print(str(integer2) + "is the largest number")
else:
    print(str(integer3) + " is the largest number")
if int(integer1) <= int(integer2) and int(integer1) <= int(integer3):
    print(str(integer1) + " is the smallest number")
elif int(integer1) >= int(integer2) and int(integer2) <= int(integer3):
    print(str(integer2) + " is the smallest number")
else:
    print(str(integer3) + " is the smallest number")
exit()
