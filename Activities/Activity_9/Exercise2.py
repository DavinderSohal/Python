my_dict = {'firstname': 'Davinder', 'lastname': 'Sohal', 'age': 24}

my_dict['address'] = 'My address'
print(list(my_dict.keys()))

my_dict['name'] = my_dict.pop('firstname') + " " + my_dict.pop('lastname')
print(my_dict)
