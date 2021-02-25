# Use the random number generator from the last slide (Flow of control ppt) to generate a random number between 0 and
# 1, then using this number, make some calculations to then generate the simulation of rolling a six sided dice (return
# a value ranging from 1 to 6)

import random

i = 1
while i <= 0.1 or i > 0.7:
    i = random.random()
print(i)
if i > 0.1 and i <= 0.2:
    print(1)
elif i > 0.2 and i <= 0.3:
    print(2)
elif i > 0.3 and i <= 0.4:
    print(3)
elif i > 0.4 and i <= 0.5:
    print(4)
elif i > 0.5 and i <= 0.6:
    print(5)
elif i > 0.6 and i <= 0.7:
    print(6)
quit()
