print("WELCOME.NOW YOU CAN BUY AN APP ONLY IN $3 AND EACH SONGS ONLY IN $7.....")
i = input("Enter the prepay amount: ")
print(i)
songs = int(i) / 7
j = (songs * 7) - int(i)
if j >= 2:
    apps = int(j) / 3
    k = int(apps * 3) - int(j)
    print("The maximum number of songs you can download from this amount is " + str(songs) + " n download " + str(
        apps) + " apps and you have " + k + "$ amount")
else:
    print("The maximum number of songs you can download from the amount is " + str(
        songs) + " and the left amount is " + str(j))
quit()
