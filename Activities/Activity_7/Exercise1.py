# Using Exercise #1 of Activity #1 random dice generator) and now implement your solution using a function instead
# Afterwards call the function multiple times so the results will be printed to the console.


import random


def dice():
    x = random.random() * 6 + 1
    print(int(x))


dice()
dice()
dice()
dice()
dice()
dice()
dice()
