# Using the following text file that contains a list of first names, give the regular expression for each of the
# following questions:
#
# https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt
#
# a) return all the names that contain two or more consecutive vowels (i.e.: ae, ou, eau etc.) (.5 point)
# 
# b) return all names that the first letter are in between letters A – M and the last letter in between  N – Z (.5
# point)
#
# c) return all names that contain a hyphen anywhere within the name, the first letter begins with a consonant and the
# last letter with a vowel (satisfies all conditions). (1 point)
#
# d) return all names that have no vowels, have duplicate consonants (such as “tt”, “ll”) and is between 3 and 10
# characters long in length. (1 point)
#
# Integrate your regex solution into a python script that opens the file and then prints the results for each
# response to the console.

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
