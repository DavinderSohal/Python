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
