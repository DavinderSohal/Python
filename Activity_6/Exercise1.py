# String Formatting Of Dates
# Create the following program:
# 	Write a python program to convert a date string input to the format YYYY-MM-DD
# 	Take a date input from the user in the form of: Day Month Year
# 	Day can be written in the following format: 1st, 2nd, 3rd, 4th, 5th ..30th, 31st
# 	Month can be written in format: Jan, Feb, Mar, Apr, May, Jun, Aug, Sep, Oct, Nov, Dec
# 	Year can be any year from 1900 to 2100
# 	Some sample output examples:
#
#           Example 1:
#           Input: date = 10th Sep 2008
#           Output: ‘2008-09-10’


print("\nSample date format to be entered by user: (day month year)")
print("""Day can be written in the following format: 1st, 2nd, 3rd, 4th, 5th ..30th, 31st
Month can be written in format: Jan, Feb, Mar, Apr, May, Jun, Aug, Sep, Oct, Nov, Dec
Year can be any year from 1900 to 2100\n""")

user_date = input("Enter date (check sample above for format): ")

split_date = user_date.split()

day = split_date[0][:-2]

if split_date[1].lower() == "jan":
    month = "01"
elif split_date[1].lower() == "feb":
    month = "02"
elif split_date[1].lower() == "mar":
    month = "03"
elif split_date[1].lower() == "apr":
    month = "04"
elif split_date[1].lower() == "may":
    month = "05"
elif split_date[1].lower() == "jun":
    month = "06"
elif split_date[1].lower() == "jul":
    month = "07"
elif split_date[1].lower() == "aug":
    month = "08"
elif split_date[1].lower() == "sep":
    month = "09"
elif split_date[1].lower() == "oct":
    month = "10"
elif split_date[1].lower() == "nov":
    month = "11"
else:
    month = "12"

year = split_date[2]

print(f"'{year}-{month}-{day}'")
