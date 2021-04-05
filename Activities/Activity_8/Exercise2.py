# Create a program that will take a string input from a user to check for the max depth of nested parenthesis given
# within that string. The max depth will be returned as an integer.
# Condition for the string input is to expect the user to input only a mix of integer values, parenthesis ‘)’ or ‘(‘
# and operators (+,-,=,/,*), no error checking is necessary on the programmers` side.
# Inputs with only parenthesis are also valid such as “() ()” and “()(()())”, these inputs would have a maximum
# nested depth of 1 and 2 respectively, whereas input such as “)(“ and “((()” would not be valid and have a depth of
# zero (as they are not properly nested)
# Further examples on next slide.

my_string = input("Enter the input with the parenthesis or without ")

i = 0
count = 0
count1 = 0
while i <= len(my_string):
    if my_string[i] == '(':
        count = count + 1
        for i in range(len(my_string)):
            if my_string[i] == '(':
                count = count + 1
            elif my_string[i] == ')':
                count1 = count1 + 1
            i = i + 1

    elif my_string[i] == ')':
        count1 = count1 + 1
    else:
        count1 = 1
        print("nothing")
        break
    i = i + 1
print("Parenthesis count: ", (count1 - 1))
