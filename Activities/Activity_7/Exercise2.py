# Change your dice function so that it will return the result instead of printing the values
# Then create another dice function called dice2 that simulates throwing two die and then calculating the sum.
# Your dice2 function should utilize the first dice function.


import random


def dice1():
    x = random.random() * 6 + 1
    return int(x)


def dice2():
    return dice1()


res1 = dice1()
res2 = dice2()

sum = res1 + res2
print("Dice 1: ", res1)
print("Dice 2: ", res2)
print("Sum:    ", sum)
