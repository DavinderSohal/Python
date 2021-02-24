c = [(0,0,1),(0,2,1), (5,2,4), (3,6,4)]    #nested list/tuple

for tup in c:         #Go over outer list
    for entry in tup: #Go over inner tuple
        print(entry)

