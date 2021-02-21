"""
Use the random number generator from the last slide (Flow of control ppt) to generate a random number between 0 and
1, then using this number, make some calculations to then generate the simulation of rolling a six sided dice (return
a value ranging from 1 to 6)
"""

import random

i = random.random()
print(i)
if 0.0 < i < 0.1:
    print("0")
elif 0.1 < i < 0.2:
    print("1")
elif 0.2 < i < 0.3:
    print("2")
elif 0.3 < i < 0.4:
    print("3")
elif 0.4 < i < 0.5:
    print("4")
elif 0.5 < i < 0.6:
    print("5")
elif 0.6 < i < 0.7:
    print("6")
else:
    print("The number is not between the dice")
quit()
