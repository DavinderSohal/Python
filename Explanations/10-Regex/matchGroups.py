# Regex group matching

import re

data_lines = ['APR 16, 13:35, S=80%']

pattern = re.compile("^([a-zA-Z]+) ?([0-9]+)")
match = pattern.search(data_lines[0])
if match:
    print(match.groups())
    print(match.group())  # match.group(0) can also be used
    print(match.group(1))
