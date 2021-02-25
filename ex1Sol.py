# Use the random number generator from the last slide (Flow of control ppt) to generate a random number between 0 and
# 1, then using this number, make some calculations to then generate the simulation of rolling a six sided dice (return
# a value ranging from 1 to 6)

import random

x = random.random()

if x >= 0 and x < 1.0 / 6:
    print(1)
elif x >= 1.0 / 6 and x < 2.0 / 6:
    print(2)
elif x >= 2.0 / 6 and x < 3.0 / 6:
    print(3)
elif x >= 3.0 / 6 and x < 4.0 / 6:
    print(4)
elif x >= 4.0 / 6 and x < 5.0 / 6:
    print(5)
else:
    print(6)

# or
# print(int(x * 6 + 1))
