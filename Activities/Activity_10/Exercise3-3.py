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
