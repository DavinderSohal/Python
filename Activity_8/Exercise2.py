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
