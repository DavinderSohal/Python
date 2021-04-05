def divide(x, y):
    result = x // y
    remainder = x % y
    return result, remainder  # Returning a tuple


# Returned tuple
print(divide(10, 3))

# Using tuple assignment
res1, res2 = divide(20, 3)
print(res1)
print(res2)
