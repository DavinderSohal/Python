# Create the following python program:
# 	This program will take an input integer ‘n’ from the user.
# 	The value will add the dot character “.” as a thousands separator and return it in string format
# 	Valid input from the user should between 0 and ‘n’ where n is any real number
# 	Some examples below for further explanation:
#
#           Example 1:
#           Input: n = 987654321
#           Output: ‘987.654.321’

n = int(input("Input integer value: "))

if n < 1000:
    print(n)
else:
    j = format(n, ',')
    print(j.replace(",", "."))
