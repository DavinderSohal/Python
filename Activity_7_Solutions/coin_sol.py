import random

def coinToss(heads_prob=0.5):   #Optional argument
    x = random.random()
    if x < heads_prob:
        return "heads"
    else:
        return "tails"

print(coinToss(heads_prob=0.7))  
print(coinToss())
