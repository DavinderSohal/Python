import re

text_file = open("firstNames.txt", 'r', encoding = 'utf8')
regex_a = r"\b(?=[a-z]*[aeiou]{2,})[a-z]+\b"
search_a = re.findall(regex_a, text_file.read())
print(search_a)
regex_b = "\b[A-M]+\w+[N-Z]"
search_b = re.findall(regex_b, text_file.read())
print(search_b)
regex_c = "[^aeiou].*-\w+[aeiou]"
search_c = re.findall(regex_c, text_file.read())
print(search_c)
regex_d = "\b\w{3,10}.([^aeiou])\1+\w+"
search_d = re.findall(regex_d, text_file.read())
print(search_d)
