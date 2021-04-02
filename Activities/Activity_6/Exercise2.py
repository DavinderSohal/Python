# Create the following python program:
# 	This program will display a mark table to the user, depending on its input.
# 	The columns represents the subjects.
# 	The rows represents the students.
# 	Algorithm to input data from the user:
#   o	Ask the user how many subjects (columns) is necessary.
#   o	Ask the user how many students (rows) is necessary.
#   o	For each student, loop and ask a mark for each subject


no_of_subjects = int(input("Enter # of subjects: "))
no_of_students = int(input("Enter # of students: "))

marks = [[None for subject in range(0, no_of_subjects)] for student in range(0, no_of_students)]

for student in range(0, no_of_students):
    for subject in range(0, no_of_subjects):
        marks[student][subject] = input(f"student {student + 1} subject {subject + 1}: ")

print(f"Marks for the {no_of_students} students\n")

for student in range(0, no_of_students):
    print(f"Student {student + 1}:    ", end = "")
    for subject in range(0, no_of_subjects):
        print(marks[student][subject], end = "  ")
    print("")
