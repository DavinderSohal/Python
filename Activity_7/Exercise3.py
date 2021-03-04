import random


def coinToss():
    x = random.random() * 2 + 1
    if int(x) == 1:
        return "Heads"
    else:
        return "Tails"


def coinTossProb(headsProb = 0.5):
    x = random.random()
    if x <= headsProb:
        return "Heads"
    else:
        return "Tails"


toss = coinToss()
toss_probability = coinTossProb(headsProb = 0.7)
toss_probability1 = coinTossProb()

print("Normal Toss     : ", toss)
print("toss probability: ", toss_probability)
print("toss probability: ", toss_probability1)
