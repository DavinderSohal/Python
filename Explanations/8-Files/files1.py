# Files - Example 1
# Will open and read Artists.csv, returning the file contents to console.
# Ensure your python file is in the same directory as the file

f = open('Artists.csv', encoding = 'utf8')
print(f.read())
