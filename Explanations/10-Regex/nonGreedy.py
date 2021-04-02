#Example of greedy regex

import re

txt = 'Hello World'

pattern1 = re.compile("([A-Za-z]+).*([A-Za-z]+)")  #greedy
pattern2 = re.compile("([A-Za-z]+).*?([A-Za-z]+)") #not greedy

print(pattern1.match(txt).groups())  # ==> ('Hello', 'd')
print(pattern2.match(txt).groups())  # ==> ('Hello', 'World')

	