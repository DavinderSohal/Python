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
