my_list = []
n = input("Enter the size of list: ")

for i in range(int(n)):
    value = input(f"Enter element {i + 1}: ")
    my_list.append(int(value))
print("User list: " + str(my_list))

while True:
    a = 0
    for i in range(1, len(my_list) - 1):
        if my_list[i] < my_list[i - 1] and my_list[i] < my_list[i + 1]:
            my_list[i] = my_list[i] + 1
            a = a + 1
        elif my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
            my_list[i] = my_list[i] - 1
            a = a + 1
        else:
            continue
    if a == 0:
        break

print("Final result: " + str(my_list))
