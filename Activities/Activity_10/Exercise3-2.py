# Modify your code to look for lines that contain either of the following artists: Pablo Picasso or Claude Monet and
# print only those two lines out.
# Return the two rows in a separate file called output.txt
# Bonus: Remove the two above lines from Artists.csv and save the new file as Artists2.csv separately.

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
