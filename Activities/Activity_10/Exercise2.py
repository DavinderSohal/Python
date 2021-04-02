
print("Name: {first_name} {last_name} \nAge: {age}".format(
    first_name = "Davinder",
    last_name = "Sohal",
    age = 24))

with open("exrc2.txt", 'w') as f:
    f.write("Name: {first_name} {last_name} \nAge: {age}\n".format(
    first_name = "Davinder",
    last_name = "Sohal",
    age = 24))
    f.write("My second Line\n")
