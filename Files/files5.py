# Files - Example 5
# Files - stdin, stdout, stderr


import sys

sys.stdout.write("Hello World")
sys.stderr.write("\nHello\n")

# Take input from user instead of using 'input()'
print("Type something")
input_str = sys.stdin.readline()
print("You typed: " + input_str)
