"""
Write a program according to the following specification:
1) Display a message asking the user to enter a student id between 0 and 9999999.
2) Get the user input.
3) Verify the student id. If the user input is bigger than 9999999 or less than 0, then display an error
message, and exit the program (Hint: use exit()).
4) Display the user input.
5) Display a message asking the user to enter a password with the length between 6 and 20.
6) Get the user input.
7) Verify the password. If the password length is not between 6 and 20, exit the program.
8) Display the user input.
9) Display a message asking the user to enter a string.
10) Display the user input.
11) Change the string to upper case.
12) Display the new string.
13) Exit the program.
"""

student_id = input("Enter a student id between 0 and 9999999: ")
if int(student_id) < 0 or int(student_id) > 9999999:
    print("Invalid value")
    exit()
print("Student ID you entered: " + student_id)

password = input("Enter a password with the length between 6 and 20: ")
length_password = len(password)
if length_password < 6 or length_password > 20:
    print("Password is not of proper length")
    exit()
print("Password you entered: " + password)

any_string = input("Enter a string: ")
print("String you entered: " + any_string)
new_uppercase_string = any_string.upper()
print("New string: " + new_uppercase_string)
exit()
