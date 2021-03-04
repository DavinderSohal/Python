# Activity 5 Solutions
# Exercise 4

x = int(input("How many marks for this student? "))
marks = []
for x in range(0, x):
    print("Mark " + str(x + 1) + ":")
    mark = int(input("  Enter: "))
    marks.append(mark)

print("The marks are: " + str(marks))
print("The average is: " + str(sum(marks) / len(marks)) + '%')
