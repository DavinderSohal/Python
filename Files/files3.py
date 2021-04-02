#Files - Example 3
#Reading specific lines from a .txt file

input = open('helloWorld.txt', 'r')
lines = input.readlines()
print(lines[1])
input.close()
