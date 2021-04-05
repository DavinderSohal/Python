# Activity 10 Solutions To Exercise 1 - Part 2

import csv

outputfile = open("output.txt", 'w')
with open('Artists.csv', 'r', errors = 'ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Male and American people
        if row['Nationality'] == 'American' and (row['Gender'] == 'Male' or (row['Gender'] == 'male')):  # Some
            # entries are lower case 'male' as well
            print(row)
            outputfile.write(str(row))
            outputfile.write('\n')
    outputfile.close()
    for row in reader:
        # Non-American and not female people :
        if row['Nationality'] != 'American' and row['Gender'] == 'Female':
            print(row)
    for row in reader:
        # Begin date before 1900
        if row['BeginDate'] < str(1900):
            print(row)
