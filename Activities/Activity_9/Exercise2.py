# Create a dictionary with keys ‘firstname’, ‘lastname’ and ‘age’, with some values assigned to each
# Add an additional key ‘address’ to the dictionary
# Print out the list of keys of your dictionary
# Create a ‘name’ key with the value as a string containing both first and last name keys. Is it possible to do this
# without typing in your name once again? If so make the modification, and when done remove the two other older keys.

my_dict = {'firstname': 'Davinder', 'lastname': 'Sohal', 'age': 24}

my_dict['address'] = 'My address'
print(list(my_dict.keys()))

my_dict['name'] = my_dict.pop('firstname') + " " + my_dict.pop('lastname')
print(my_dict)
