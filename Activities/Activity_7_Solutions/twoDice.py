import random


def dice():
    x = random.random()
    return 1 + int(x * 6)


def dice2():
    d1 = dice()
    d2 = dice()
    return d1 + d2


result = dice()
print("Results of 1 dice roll:  " + str(result))

result2 = dice2()
print("Sum of 2 dice: " + str(result2))
