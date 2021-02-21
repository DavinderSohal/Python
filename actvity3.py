"""
An online music and apps store offers all apps for 3$ each and all songs for 7$ each. The store requires members to
prepay any amount of money they wish, and then download as many apps or as many songs accordingly. You are required
to write a program that would ask the user for the amount that he/she will pay, then display two messages indicating:
- the maximum number of apps that can be downloaded, and how much funds will remain in the account after that, if any.
- the maximum number of songs that can be downloaded, the number of apps that can be downloaded after that if funds
allow, and how much funds will remain in the account after that, if any.
For this exercise, assume that the user will always enter a valid integer value that is >= 0, and within the limit of
the integer range.
An example of how your program should behave is indicated on the next two slides
"""

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
