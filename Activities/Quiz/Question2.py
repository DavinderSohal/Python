arr1_length = int(input("Number of items in array 1: "))
arr2_length = int(input("Number of items in array 2: "))
arr3_length = int(input("Number of items in array 3: "))

arr1 = []
arr2 = []
arr3 = []

for item1 in range(0, arr1_length):
    arr1.append(int(input(f"Enter element {item1 + 1}: ")))

for item2 in range(0, arr2_length):
    arr2.append(int(input(f"Enter element {item2 + 1}: ")))

for item3 in range(0, arr3_length):
    arr3.append(int(input(f"Enter element {item3 + 1}: ")))

set_arr1 = set(arr1)
set_arr2 = set(arr2)
set_arr3 = set(arr3)

print("Array 1: " + str(arr1))
print("Array 2: " + str(arr2))
print("Array 3: " + str(arr3))

if (set_arr1 & set_arr2) & set_arr3:
    print(list((set_arr1 & set_arr2) & set_arr3))
else:
    print("No common element")
