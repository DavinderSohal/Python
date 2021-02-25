# 1. Create a variable containing the string “I hate Python”
# 2. Turn it into a more positive string: “I love Python” using replace method and print the output
# 3. Finally print out the middle letter of the new string using the len method (do not simply count the letters and
# print the letter without using the len() method!)

my_string = "I hate Python"

replace_str = my_string.replace("hate", "love")
print(replace_str)

mid = len(my_string) // 2
print("Middle letter: " + replace_str[mid])
