import re

text = "CEGEP Gaspesie"
pattern = re.compile("([A-Za-z]+).*([A-Za-z]+)")

print(pattern.match(text).groups())	# what is the output? will be groups.. which ones?


