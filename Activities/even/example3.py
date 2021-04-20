try:
    print(1 / 10)
except:
    print("An execption occur")
try:
    print(hello_world)
except NameError:
    print("An exception occur, you missed something ")
d = [1, 2, 3, 4]
try:
    print(d[4])
except IndexError:
    print("d[4] doesn't exit.Only available values of list are " + str(d[1:]))
