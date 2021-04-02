def rearrange_array():
    first_list = x[:array_length]
    second_list = x[array_length:]

    sorted_array = []
    first_list_count = 0
    second_list_count = 0

    for val in range(array_length * 2):
        if val == 0:
            sorted_array.insert(val, first_list[first_list_count])
            first_list_count = first_list_count + 1
        elif val % 2 == 0:
            sorted_array.insert(val, first_list[first_list_count])
            first_list_count = first_list_count + 1
        else:
            sorted_array.insert(val, second_list[second_list_count])
            second_list_count = second_list_count + 1

    print("Sorted array: ", sorted_array)


array_length = int(input("If 2*n is length of array, enter value of n: "))

x = []

for item in range(2 * array_length):
    x.append(int(input(f"Enter element {item + 1}: ")))

print("User input: ", x)

rearrange_array()
