number_of_marks = input("How many marks for this student? ")
mark = []
i = 1
while i <= int(number_of_marks):
    mark.append(input(f"Mark {i}: "))
    i += 1

summation = 0
print("The marks are ", end = "")
for val in mark:
    print(val, end = ", ")
    summation += int(val)

print("\nThe average is: %(average)s%%" % {"average": round(summation / int(number_of_marks), 2)})
