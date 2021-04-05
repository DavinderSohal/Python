# Write a program that incorporates an algorithm with a function that will check whether or not a string is in a
# valid password format with the following rules:
#
# A password must have at least ten characters.
# A password consists of only letters, digits and symbol(s).
# A password must contain at least two digits.
# A password must contain at least one uppercase letter
# A password must contain at least one special symbol
#
# Your program should continue to prompt the user until he/she enters a valid password.
# Your program may not use any regex (regular expressions)

def valid_password(password):
    temp = False
    digit_count = 0
    upper_count = 0
    special_count = 0

    if len(password) > 10:
        for index in range(len(password)):
            if (password[index] == "1" or password[index] == "2" or password[index] == "3" or password[index] == "4"
                    or password[index] == "5" or password[index] == "6" or password[index] == "7"
                    or password[index] == "8" or password[index] == "9" or password[index] == "0"):
                digit_count = digit_count + 1
            if password[index].isupper():
                upper_count = 1
            if (password[index] == "@" or password[index] == "#" or password[index] == "!"
                    or password[index] == "~" or password[index] == "$" or password[index] == "%"
                    or password[index] == "^" or password[index] == "&" or password[index] == "*"
                    or password[index] == "(" or password[index] == ")" or password[index] == "-"
                    or password[index] == "+" or password[index] == "/" or password[index] == ":"
                    or password[index] == "." or password[index] == "," or password[index] == "<"
                    or password[index] == ">" or password[index] == "?" or password[index] == "|"):
                special_count = 1

            if upper_count and digit_count and special_count > 0:
                temp = True

    return temp


print("""A password must have at least ten characters.
A password consists of only letters, digits and symbol(s).
A password must contain at least two digits.
A password must contain at least one uppercase letter
A password must contain at least one special symbol""")

password = input("Enter the password (must follow above mentioned conditions): ")

result = valid_password(password)
while not result:
    print("Invalid Password")
    password = input("Enter the password (must follow above mentioned conditions): ")
    result = valid_password(password)

print(f"\nPassword successfully set: {password}")
