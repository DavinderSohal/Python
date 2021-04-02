import random
x = random.random()
if x >= 0 and x < 0.5:
    print("Heads")
elif x >= 0.5 and x < 1.0:
    print("Tails")
else:
    print("Number not a probability")
    
