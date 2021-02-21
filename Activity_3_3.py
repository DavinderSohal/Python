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

amount = input("Enter the amount: ")
number_of_apps = int(amount) // 3
balance = int(amount) % 3
print("Maximum # of apps that can be downloaded: " + str(number_of_apps))
print("balance after downloading apps: " + str(balance))

number_of_songs = int(amount) // 7
balance = int(amount) % 7
number_of_apps = balance // 3
balance = balance % 3
print("\nMaximum # of songs that can be downloaded: " + str(number_of_songs))
print("Maximum # of apps that can be downloaded with remaining balance: " + str(number_of_apps))
print("balance after downloading apps: " + str(balance))
quit()
