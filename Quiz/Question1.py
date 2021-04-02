my_string = input("Enter a string: ")
list_string = list(my_string)

my_array = []
print("Enter the elements of array (same size as that of string)")

for i in range(len(my_string)):
    value = input(f"Enter element {i + 1}: ")
    my_array.append(value)

temp_list = ["*"] * len(my_string)
for i in range(0, len(list_string)):
    temp_list.pop(int(my_array[i]))
    temp_list.insert(int(my_array[i]), list_string[i])

final_string = ""
for item in temp_list:
    final_string += item

print("User input: " + my_string)
print("Re-arranged: " + final_string)
