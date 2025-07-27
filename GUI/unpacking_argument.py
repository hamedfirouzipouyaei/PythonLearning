def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(2, 3, 4))  # Output: 24

