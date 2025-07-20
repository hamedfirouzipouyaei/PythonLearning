print(4%2) # Modulus function returns the remainder of the division
print(5%2) 

var = 6
print(var)

x = 10
y = 4

print("Addition:", x + y)  # Addition
print("Subtraction:", x - y)  # Subtraction
print("Multiplication:", x * y)  # Multiplication
print("Division:", x / y)  # Division
print("Floor Division:", x // y)  # Floor Division
print("Exponentiation:", x ** y)  # Exponentiation
print("Modulus:", x % y)  # Modulus
print("Equality:", x == y)  # Equality
print("Inequality:", x != y)  # Inequality
print("Greater than:", x > y)   # Greater than
print("Less than:", x < y)   # Less than
print("Greater than or equal to:", x >= y)  # Greater than or equal to
print("Less than or equal to:", x <= y)  # Less than or equal to
print("Logical AND:", x > 5 and y < 5)  # Logical AND
print("Logical OR:", x > 5 or y > 5)  # Logical OR


single_quote = 'This is a single quote string'
double_quote = "This is a double quote string"

print(single_quote)
print(double_quote)

using_single_in_double = 'This is a "double quote" inside single quotes'
print("Using single quotes in double quotes:", using_single_in_double)
using_double_in_single = "This isn't just an example, it's a test"
print("Using double quotes in single quotes:", using_double_in_single)


num = 12
name= "Sam"
print('My name is {} and my number is {}'.format(name, num))
print(f'My name is {name} and my number is {num}')  # f-string formatting
print("My name is {one} and my number is {two}".format(one=name, two=num))  # format method with named placeholders

s = "Hello, World!"
print(s[0])  # Accessing the first character
print(s[-1])  # Accessing the last character
print(s[1:4])  # Slicing from index 1 to 3
print(s[1:])  # Slicing from index 1 to the end
print(s[:3])  # Slicing from the start to index 2
print(s[::2])  # Slicing with a step of 2

l1 = [1, 2, 3, 4, 5] # List of integers
l2 = ["a", "b", "c"]  # List of strings

l2.append("d")  # Adding an element to the end of the list
print("List after appending:", l2)

l2.insert(1, "x")  # Inserting an element at index 1
print("List after inserting:", l2)

print("Length of l1:", len(l1))  # Length of the list
print("Length of l2:", len(l2))  # Length of the list

print(l2[1:3])  # Slicing the list from index 1 to 2
print(l2[1:])  # Slicing the list from index 1 to the end
print(l2[:3])  # Slicing the list from the start to index 2 

l3 = [1, 2, 3, 4, 5, [6, 7, 8]]  # Nested list
print("Nested list:", l3)
print(l3[2])  # Accessing the third element
print(l3[5][1])  # Accessing the second element of the nested list


d1 = {"name": "Alice", "age": 30}  # Dictionary with string keys
d2 = {"city": "New York", "country": "USA"}  # Dictionary
d3 = {1: "one", 2: "two"}  # Dictionary with integer keys
print("Dictionary d1:", d1)
print("Dictionary d2:", d2)
print("Dictionary d3:", d3)

d4 = {"name": ["Alice", "Bob"], "age": [30, 25]}  # Dictionary with lists as values
print("Dictionary with lists as values:", d4)
print("Accessing d1['name']:", d1["name"])  # Accessing a value by key
print("Accessing d4['name'][1]:", d4["name"][1])  # Accessing a value in a list within a dictionary


t1 = (1, 2, 3)  # Tuple of integers
t2 = ("a", "b", "c")  # Tuple of strings    
print("Tuple t1:", t1)
print("Tuple t2:", t2)

# Demonstrating tuple immutability with try-except
try:
    t1[0] = 10  # Tuples are immutable, this will raise an error
except TypeError as e:
    print(f"Error caught: {e}")
    print("t1[0] = 10 will raise an error because tuples are immutable.")
    print("This demonstrates that tuples are immutable - you cannot modify their elements")

print("Accessing t1[1]:", t1[1])  # Accessing


s1 = {1, 2, 3}  # Set of integers
s2 = {"a", "b", "c"}  # Set of strings
s3 = {1, 2, 3, "string", (4, 5, 6), True}  # Valid set with hashable types only
print("Set s1:", s1)
print("Set s2:", s2)
print("Set s3:", s3)

# Demonstrating set error with try-except
try:
    invalid_set = {1, 2, {"key": "value"}}  # This will raise an error
except TypeError as e:
    print(f"Set error caught: {e}")
    print("Sets can only contain hashable (immutable) objects like numbers, strings, and tuples")

print("Accessing s1:", s1)  # Accessing a set
print("Accessing s2:", s2)  # Accessing a set
print("Accessing s3:", s3)  # Accessing a set

if 1 < 2:
    print("1 is less than 2")
    # This is a simple if statement

if 1 == 2:
    print("1 is equal to 2")
else:
    print("1 is not equal to 2")

seq  = [1, 2, 3, 4, 5]
for i in seq:
    print("Current value:", i)  # Looping through a sequence

i = 1

while i < 6:
    print("Current value in while loop:", i)  # Looping with a condition
    i += 1  # Incrementing the counter
    if i == 3:
        print("Skipping 3")
        continue  # Skipping the rest of the loop when i is 3
    
    
    

for x in range(0, 5):
    if x == 3:
        print("Skipping 3 in range loop")
        continue  # Skipping the rest of the loop when x is 3
    print("Current value in range loop:", x)


seq2 = list(range(0, 10))  # Creating a sequence from 0 to 9
print(seq2)

com = [num**2 for num in seq2]  # List comprehension to square each number in seq2
print("List comprehension result:", com)  # Printing the result of list comprehension


def func1(parm1, parm2=3):
    """
    This function takes two parameters and returns their sum.
    If the second parameter is not provided, it defaults to 3.
    """
    print("Function with two parameters called")
    return parm1 + parm2  # Returning the sum of the two parameters

print("Result of func1:", func1(5, 10))  # Calling the function with two arguments
print("Result of func1 with default:", func1(5))  # Calling the function with one argument



def times_two(num):
    """
    This function takes a number and returns it multiplied by two.
    """
    return num * 2  # Returning the number multiplied by two    

seq3 = [1, 2, 3, 4, 5]
result = list(map(times_two, seq3))  # Using map to apply times_two to each element in seq3
print("Result of map with times_two:", result)  # Printing the result of the map

result1 = list(map(lambda x: x * 2, seq3))  # Using a lambda function to achieve the same result
print("Result of map with lambda:", result1)  # Printing the result of the lambda

result2 = list(filter(lambda num: num % 2 == 0, seq3))
print("Result of filter with lambda:", result2)  # Printing the result of the filter

x = [(1, 2), (3, 4), (5, 6)]  # List of tuples
for (a, b) in x:
    print("Tuple values:", a, b)  # Unpacking tuples in a loop

