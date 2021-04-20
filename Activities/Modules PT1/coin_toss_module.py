import random


def coin_toss(heads_prob = 0.5):
    x = random.random()
    if x < heads_prob:
        return "heads"
    else:
        return "tails"
