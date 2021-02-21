height = input("Enter your height(in cms): ")
if int(height) < 120:
    print("You do not meet the height requirements(must be more than 120cm). You can't this ride")
elif int(height) > 120 and int(height) < 130:
    print("To go on this ride, you must be with an adult.")
else:
    print("You can go for the ride. Thanku")
quit()
