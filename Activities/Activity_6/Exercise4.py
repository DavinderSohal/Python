# Create the following program:
# 	Write a python program to display the marks in the class of 20 students
# 	The marks of the students will be stored in a list or tuple (of your choice)
# 	Each element will be an integer between 0 and 9 (inclusively)
# 	The histogram will have a series of stars for each possible value of the mark

import random

marks = []

for mark in range(0, 20):
    marks.append(round(random.random() * 9))

for x in range(0, 10):
    count = 0
    for y in range(0, 20):
        if marks[y] == x:
            count += 1
    stars = "*" * count
    print(x, ": ", stars)
