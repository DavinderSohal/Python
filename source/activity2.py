import random

i = random.random()
print(i)
if 0.0 < i < 0.1:
    print("0")
elif 0.1 < i < 0.2:
    print("1")
elif 0.2 < i < 0.3:
    print("2")
elif 0.3 < i < 0.4:
    print("3")
elif 0.4 < i < 0.5:
    print("4")
elif 0.5 < i < 0.6:
    print("5")
elif 0.6 < i < 0.7:
    print("6")
else:
    print("The number is not between the dice")
quit()
