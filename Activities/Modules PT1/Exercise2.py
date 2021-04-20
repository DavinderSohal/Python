import random

import numpy as np

sum_of_dice = []

for i in range(1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_of_dice.append(dice1 + dice2)

average = np.average(sum_of_dice)
print("Average: " + str(average))
