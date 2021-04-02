#Files - Example 6
#Files - csv

import csv

with open('writeData.csv', mode = 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Programming language', 'Creator', 'Date', 'File Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])