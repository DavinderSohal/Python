# Create a coin toss function that simulates tossing a coin (returns heads or tails).
# Next, change the function so that it takes an argument that allows the programmer to specify a percentage chance of
# getting heads. For example calling the function like: coinToss(headsProb = 0.7) where coinToss is the name of the
# function. Heads should now come up 70% of the time
# Afterwards, make an additional change so that headsProb is an optional argument in the function and if no argument
# is given, the coin toss will be fair (50/50)


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
