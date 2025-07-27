name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")


age = int(input("Enter your age: ") if age.isdigit() else 0)
print("You are {} days old.".format(age * 365))