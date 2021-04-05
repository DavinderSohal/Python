# Using Artists.csv, write a query that returns all lines that are female artists only, with begin date greater than
# 1950 but no greater than 2000
# Write a query that will return all lines of British Male artists, who's first names starts with the letter ‘A’ and
# has an end date earlier than 1990
# Write a query that will write to a file all lines that have Japanese Artists who’s difference of end date and begin
# date exceeds 100 years. I.e. if artist begins in 1900 and ends in 2005, then they would be included in the output (
# 2005-1900 = 105 years)
# Write a query that will write and find to a file the artist who’s been at the Museum the longest (the widest gap
# between Begin Date and End Date)

import csv

outputfile = open("output.txt", 'w')
with open('Artists.csv', 'r', errors = 'ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Gender'] == 'Female' or row['Gender'] == 'female':
            if row['BeginDate'] < str(2000) or row['BeginDate'] > str(1950):
                print(row)

    for row in reader:
        if row['Nationality'] == 'British' and (row['Gender'] == 'Male' or (row['Gender'] == 'male')):
            if row['EndDate'] < str(1990):
                if row['DisplayName'][0] == 'A':
                    print(row)

    for row in reader:
        if row['Nationality'] == 'Japanese':
            if (int(row['EndDate']) - int(row['BeginDate'])) >= 100:
                print(row)
                outputfile.write(str(row))
                outputfile.write('\n')
    outputfile.close()
