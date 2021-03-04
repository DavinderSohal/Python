# Activity 5 Solutions
# Exericse 3

number_list = [6, 9, 4, 8, 7, 1, 2]

# While Loop
i = 0
while i < len(number_list):
    print(number_list[i])
    i += 1

# For loop
for entry in number_list:
    print(entry)

# Printing all elements that are larger than their neighbor
for i in range(1, len(number_list)):
    if number_list[i] > number_list[i - 1]:
        print(number_list[i])
