from turtle import Turtle, Screen
from prettytable import PrettyTable
import user_class as user

user1 = user.User("John Doe", "john@example.com", 1)
user1.age = 25

print(f"User Name: {user1.name}")
print(f"User Email: {user1.email}")
print(f"User ID: {user1.id}")
print(f"User Age: {user1.age}")
print(f"User Year of Birth: {user1.year_of_birth(2025)}")
print(f"Is User Adult? {user1.is_adult()}")