#Files - Example 6
#Files - csv

from pathlib import Path
import csv

data = Path('C:/Users/lbran/Desktop/Artists.csv')
myPath = data
with open(myPath, errors='ignore') as f:
    data = csv.reader(f)
    for row in data:
        print(row)
        