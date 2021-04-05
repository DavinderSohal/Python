import re

dict_filename = "firstNames.txt"

# Open file
dict_file = open(dict_filename)

pattern = re.compile(r"^(.).*\1$", re.IGNORECASE)  # Regex Pattern, 'r' prefix denotes raw string, escape sequence
# such as \n are not parsed

for line in dict_file.readlines():
    if pattern.match(line):
        print(line)
