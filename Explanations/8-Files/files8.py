# Files - Example 7
# Files - csv
# Printing a particular column from a csv file

import csv

with open('Artists.csv', errors = 'ignore') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['DisplayName'])
