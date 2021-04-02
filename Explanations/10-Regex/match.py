#The match function

import re

p = re.compile('[a-z]+') 
print(p)
print(p.match("world"))
print(p.match("World"))
