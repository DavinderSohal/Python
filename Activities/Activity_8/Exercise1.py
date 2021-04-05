# You are given some array called “x” that contains 2 * n elements in the arrangement of [x1, x2,…,xn,y1,y2,
# …yn] (where n is the elements contained the in the array)
# Create a function that will return the array in the form of [x1,y1,x2,y2,…,xn,yn]
# Sample example 1:
#    User input: [1,2,3,4,4,3,2,1] and n = 4
#    Output: [1,4,2,3,3,2,4,1]
# Sample example 2:
#    User input: [1,1,2,2] and n = 2
#    Output: [1,2,1,2]

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
