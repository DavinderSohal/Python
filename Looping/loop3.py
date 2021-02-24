for i in range(1,5):  
    if i==3:
        continue	# start on next iteration (skips print)  
    print(i)


print("")


l = range(1, 10)
for x in l:
    print(x)
    if x == 12:
        break  #Escape/break out of the for loop at this line
    else:
        print("Element not found!")
    
