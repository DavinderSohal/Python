import csv

outputfile = open("output.txt", 'w')
with open('Artists.csv', 'r', errors = 'ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['DisplayName'] == 'Pablo Picasso' or row['DisplayName'] == 'Claude Monet':
            print(row)
            outputfile.write(str(row))
            outputfile.write('\n')
    outputfile.close()
