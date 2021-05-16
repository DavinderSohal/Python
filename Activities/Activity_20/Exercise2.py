distance_in_km = float(input("\nEnter linear distance in kilometers (km): "))
nautical_mile = 0.54 * distance_in_km
statute_mile = 1.151 * nautical_mile
furlongs = 8 * statute_mile
print("The distance in NM is:", round(nautical_mile, 5))
print("The distance in SM is:", round(statute_mile, 5))
print("The distance in Furlong is:", round(furlongs, 5))
print("End of linear converter program.")
