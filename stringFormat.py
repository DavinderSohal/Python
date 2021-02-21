# New way to string format
print('String Format: ${2} {1} {0} '.format(0, 'one', 2.34))

# New way to string format
print('{aNumber} {aString} ${aFloat}'.format(
    aNumber = 9,
    aString = 'HelloWorld',
    aFloat = 3.03))

# Old way to string format
print('String Modulo: %d %s $%.2f' % (0, 'one', 2.34))

# Old way to string format
print("I have %(n_apples)s apples and %(n_pears)s pears." % {"n_apples": 5, "n_pears": 7})

print("3%(sep)s14 2%(sep)s72 1%(sep)s41" % {"sep": "."})

exit()  # To quit your program
