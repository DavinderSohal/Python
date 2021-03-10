# # course = "math"
# age = 30
# dob = int(input("age: "))
# after = age - dob
# # print(f"course: ({course})")
# print(f"dob: {dob}")
# print(f"after: {after}")


def new_list(n):
    list2 = n[:array]
    list3 = n[array:]
    print(list2, list3)
    new_list2 = []
    list2_elements = 0
    list3_elements = 0
    for i in range(0, array*2):
        if i == 0:
            new_list2.insert(i, list2[list2_elements])
            list2_elements = list2_elements + 1
        elif i%2 == 0:
            new_list2.insert(i, list3[list3_elements])
            list3_elements = list3_elements + 1
        else:
            new_list2.insert(i, list2[list2_elements])
            list2_elements = list2_elements + 1
    return new_list2





array = int(input("Enter the number of array"))
list = []
for i in range(0, array*2):
    values = int(input())
    list.append(values)
print(list)
print(new_list(list))