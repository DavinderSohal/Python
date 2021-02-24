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
