#Example of using the search function with regular expressions

import re

p = re.compile('[a-z]+[0-9]') 
str = 'cat808'
match = re.search(p, str)

if match:
  print ('found', str) 
else:
  print ('did not find')






