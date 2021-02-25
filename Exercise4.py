# Write a complete application that inputs three integers from the user and displays the sum, average, product,
# smallest and largest of these numbers. The average calculation should result in a floating point number.
# For example, if the input is “1,2,3” the output should be:
#    Sum: 6
#    Average: 2
#    Product: 6
#    Smallest: 1
#    Largest: 3

i = input("Enter three numbers: ")
j = input()
k = input()
Sum = int(i) + int(j) + int(k)
print("Sum: " + str(Sum))
Average = int(Sum) / 3
print("Average : " + str(Average))
Product = int(i) * int(j) * int(k)
print("Product : " + str(Product))
if int(i) >= int(j) and int(i) >= int(k):
    print(str(i) + "is the largest number")
elif int(j) >= int(i) and int(j) >= int(k):
    print(str(j) + "is the largest number")
else:
    print(str(k) + " is the largest number")
if int(i) <= int(j) and int(i) <= int(k):
    print(str(i) + " is the smallest number")
elif int(i) >= int(j) and int(j) <= int(k):
    print(str(j) + " is the smallest number")
else:
    print(str(k) + " is the smallest number")
quit()
