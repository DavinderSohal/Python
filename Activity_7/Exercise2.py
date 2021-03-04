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
