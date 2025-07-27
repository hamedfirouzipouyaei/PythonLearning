def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def func1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def named(**kwargs):
    print(kwargs)

def named2(name, age):
    print(name, age)

print(multiply(2, 3, 4))  # Output: 24
func1(name="Alice", age=30, city="New York")  # Output: name: Alice, age: 30, city: New York
named(name="Bob", age=25)  # Output: {'name': 'Bob', 'age': 25}

details = {'name': 'Charlie', 'age': 35}
named2(**details)  # Output: Charlie 35