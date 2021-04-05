# Activity 6 - Exercise 1 Solution
# String formatting of a date input

date = input("Enter: ")

d, m, y = date.split()
day = int(d[:-2])
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(m) + 1
year = int(y)
print("{:04d}-{:02d}-{:02d}".format(year, month, day))
