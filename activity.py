print("WELCOME TO THE AMUSEMENT PARK")
print("SOME OF THE RIDES HAVE THE RESTRICTIONS SO, PLEASE FILL YOUR INFORMATION")
i = input("Enter the height of yours in cm: ")
if 120 < int(i) < 130:
    print("You must an adult with you to go on this ride")
elif int(i) > 130:
    print("You are eligible for this ride alone.ENJOY...")
else:
    print("SORRY.You are not eligible for this ride")
quit()
