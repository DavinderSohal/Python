# while loop
# Modify the code removing the x += 1 portion and run the code.
# What happens?
# Now modify the code to print the numbers but in reverse order
# Lastly, modify the code to print the numbers 1 through 10 which are not divisible by 3

x = 1
while x < 5:
    print(x)
    x += 1  # removing this line of code will make this an infinite loop

print("Hello")

# printing number in reverse
x = 4
while x > 0:
    print(x)
    x -= 1

print("Hello")

# printing number divisible by 3
x = 1
while x <= 10:
    if not x % 3 == 0:
        print(x)
    x += 1
