# Files - Example 6
# Files - csv

import csv
from pathlib import Path

data = Path('C:/Users/sohal/Desktop/Artists.csv')
myPath = data
with open(myPath, errors = 'ignore') as f:
    data = csv.reader(f)
    for row in data:
        print(row)
