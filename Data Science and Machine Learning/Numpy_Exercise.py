import numpy as np

a_zeros = np.zeros(10)
print("Array of zeros:", a_zeros)

a_ones = np.ones(10)
print("Array of ones:", a_ones)

a_fives_1 = np.ones(10) * 5
print("Array of fives:", a_fives_1)

a_fives_2 = np.full(10, 5)  # Creates an array of fives using full
print("Array of fives using full:", a_fives_2)

a_integer = np.arange(10, 51, 1)
print("Array of integers from 10 to 50:", a_integer)

a_integer_even = np.arange(10, 51, 2)
print("Array of even integers from 10 to 50:", a_integer_even)

matrix_1 = np.arange(0,9).reshape(3, 3)
print("3x3 Matrix:\n", matrix_1)

matrix_2 = np.eye(3)  # Creates a 3x3 identity matrix
print("3x3 Identity Matrix:\n", matrix_2)

a_random = np.random.rand(1)
print("Random value between 0 and 1:", a_random)

a_random_normal = np.random.randn(25)  # Creates an array of 25 random values from a normal distribution
print("25 Random values from a normal distribution:\n", a_random_normal)

matrix_3 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print("10x10 Matrix with values from 0 to 1:\n", matrix_3)

a_even_space = np.linspace(0, 1, 20)  # Creates an array of 20 evenly spaced values between 0 and 1
print("20 Evenly spaced values between 0 and 1:", a_even_space)

mat = np.arange(1, 26).reshape(5, 5)
print("5x5 Matrix:\n", mat)

print("A slice of the matrix (rows 3 to 5 and columns 2 to 5):\n", mat[2:5, 1:5])
print("Element at row 4, column 6:", mat[3, 4])  # Accessing a specific element
print("A slice of the matrix (rows 1 to 3 and columns 2):\n", mat[0:3, 1])
print("A slice of the matrix:\n", mat[4, :])  # Accessing the last row
print("A slice of the matrix:\n", mat[3:, :])

print("Sum of all the elements in the matrix:" , mat.sum())
print("Standard deviation of the matrix:", mat.std())   
print("Sum of each column in the matrix:", mat.sum(axis=0))  # Sum along columns
print("Sum of each row in the matrix:", mat.sum(axis=1))  # Sum along rows