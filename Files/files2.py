#Files - Example 2
#Using pathlib to provide a specific path to where files are located

from pathlib import Path

data = Path('C:/Users/sohal/Desktop/Artists.csv')
file_to_open = data
f = open(file_to_open, encoding='utf8')
print(f.read())
