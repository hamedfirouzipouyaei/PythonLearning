"""
NumPy (Numerical Python) - Introduction and Overview

NumPy is the fundamental package for scientific computing in Python. It provides:

1. POWERFUL N-DIMENSIONAL ARRAY OBJECT:
   - Fast and efficient multidimensional array operations
   - Broadcasting capabilities for operations on arrays of different shapes
   - Element-wise operations and mathematical functions
   - Advanced indexing and slicing capabilities

2. MATHEMATICAL FUNCTIONS:
   - Comprehensive collection of mathematical functions
   - Linear algebra operations (matrix multiplication, decomposition, etc.)
   - Fourier transforms and random number generation
   - Statistical functions and aggregations

3. TOOLS FOR INTEGRATING WITH C/C++ AND FORTRAN:
   - Easy integration with existing codebases
   - Performance optimization through compiled extensions

4. KEY FEATURES:
   - Memory efficient operations
   - Vectorized computations (faster than pure Python loops)
   - Broadcasting rules for arithmetic operations
   - Universal functions (ufuncs) for element-wise operations

5. COMMON USE CASES:
   - Data analysis and manipulation
   - Scientific computing and research
   - Machine learning preprocessing
   - Image and signal processing
   - Mathematical modeling and simulations

6. CORE CONCEPTS:
   - ndarray: The main array object (N-dimensional array)
   - dtype: Data types for array elements
   - Shape: Dimensions of the array
   - Axis: Direction along which operations are performed
   - Broadcasting: Rules for operations on arrays with different shapes

NumPy serves as the foundation for many other scientific Python libraries
including pandas, scikit-learn, matplotlib, and scipy.

Installation: pip install numpy
Import convention: import numpy as np
"""

list_1 = [1, 2, 3, 4, 5]

import numpy as np

array_1 = np.array(list_1)

print("List:", list_1)
print("Array:", array_1)

matrix_1 = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix_1)    


a_1 = np.arange(10)  # Creates an array with values from 0 to 9
a_2 = np.linspace(0, 1, 5)  # Creates an array with 5
a_3 = np.arange(0, 11, 2)  # Creates an array with values from 0 to 8 with a step of 2
print("Array a_1:", a_1)
print("Array a_2:", a_2)
print("Array a_3:", a_3)

a_4 = np.zeros((2, 3))  # Creates a 2x3 array filled with zeros
a_5 = np.ones((3, 2))   # Creates a 3x2 array filled with ones
a_6 = np.eye(3)         # Creates a 3x3 identity matrix
print("Array a_4 (zeros):\n", a_4)
print("Array a_5 (ones):\n", a_5)
print("Array a_6 (identity matrix):\n", a_6)

a_7 = np.random.rand(3, 2)  # Creates a 3x2 array with random values
a_8 = np.random.randint(0, 10, (2, 3))  # Creates a 2x3 array with random integers between 0 and 10 [not inclusive of 10]
print("Array a_7 (random values):\n", a_7)
print("Array a_8 (random integers):\n", a_8)

a_9 = np.random.randn(3, 2)  # Creates a 3x2 array with random values from a normal distribution
a_10 = np.random.choice([1, 2, 3, 4, 5], size=(2, 3))  # Creates a 2x3 array with random choices from the list
print("Array a_9 (normal distribution):\n", a_9)
print("Array a_10 (random choices):\n", a_10)

a_11 = a_1.reshape(2, 5)  # Reshapes a_1 into a 2x5 array
print("Array a_11 (reshaped a_1):\n", a_11)

a_12 = np.random.randint(0, 50, (3,5))  # Creates a 3x5 array with random integers between 0 and 50

print("Maximum value in a_1:", np.max(a_12)  )  # Finds the maximum value in a_1
print("Argmax of a_1:", np.argmax(a_12))  # Finds the index of the maximum value in a_1
print("Minimum value in a_1:", np.min(a_12))  # Finds the minimum value in a_1
print("Argmin of a_1:", np.argmin(a_12))  # Finds the index of the minimum value in a_1
print("Sum of elements in a_1:", np.sum(a_12))  # Calculates the sum of elements in a_1
print("Mean of elements in a_1:", np.mean(a_12))  # Calculates the mean of elements in a_1
print("Standard deviation of elements in a_1:", np.std(a_12))        
print("Data type of a_12:", a_12.dtype)  # Prints the data type of elements in a_12



# Indesxing and Slicing in an array
ar_1 = np.arange(0, 11)
print("Original array ar_1:", ar_1)
print("Element at index 5:", ar_1[5])  # Accessing a single element
print("Elements from index 2 to 5:", ar_1[2:6])
print("Elements from index 2 to the end:", ar_1[2:])
print("Elements from the start to index 5:", ar_1[:6])
print("Elements with a step of 2:", ar_1[::2])  #
print("Last element:", ar_1[-1])  # Accessing the last element
print("Last three elements:", ar_1[-3:])  # Accessing the last three elements
print("Elements from index 2 to 5 with a step of 2:", ar_1[2:6:2])  # Slicing with a step
print("Elements from index 2 to 5 with a step of -1:", ar_1[5:2:-1])  # Slicing with a negative step
print("Elements from index 2 to 5 with a step of -1 (reversed):", ar_1[5:1:-1])  # Slicing with a negative step in reverse order

ar_1[2:5] = 99  # Modifying a slice
print("Modified array ar_1:", ar_1) 

ar_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array ar_2:\n", ar_2)
print("Element at row 1, column 2:", ar_2[1, 2])  # Accessing a specific element
print("Row 1:", ar_2[1])  # Accessing a specific row
print("Column 2:", ar_2[:, 2])  # Accessing a specific column
print("Elements from row 0 to row 1, and column 0 to column 1:\n", ar_2[0:2, 0:2])  # Slicing a 2D array
print("Elements from row 1 to the end, and column 1 to the end:\n", ar_2[1:, 1:])  # Slicing a 2D array with a step
print("Elements from row 0 to row 2, and column 0 to column 2:\n", ar_2[0:3, 0:3])  #
print("Elements from row 0 to row 2, and column 0 to column 2 with a step of 2:\n", ar_2[0:3:2, 0:3:2])  # Slicing a 2D array with a step
print("Elements from row 0 to row 2, and column 0 to column 2 with a step of -1:\n", ar_2[0:3:2, 0:3:2][::-1])  # Slicing a 2D array
print("Elements from row 0 to row 2, and column 0 to column 2 with a step of -1 (reversed):\n", ar_2[0:3:2, 0:3:2][::-1])  # Slicing a 2D array with a step in reverse order    

ar_3 = ar_1[ar_1 > 5]  # Boolean indexing
print("Elements in ar_1 greater than 5:", ar_3)  # Prints the elements in ar_1 that are greater than 5


# Numpy operations
a_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original array a_1:", a_1)
print("Square of each element in a_1:", a_1 ** 2)
print("Square root of each element in a_1:", np.sqrt(a_1))
print("Logarithm (base e) of each element in a_1:", np.log(a_1))
print("Logarithm (base 10) of each element in a_1:", np.log10(a_1))
print("Subtracting 5 from each element in a_1:", a_1 - 5)
print("Adding 5 to each element in a_1:", a_1 + 5)
print("Multiplying each element in a_1 by 2:", a_1 * a_1)
print("Dividing each element in a_1 by 2:", a_1 / 2)
print("Exponentiation of each element in a_1 (e^x):", np.exp(a_1))
print("Sine of each element in a_1:", np.sin(a_1))
print("Cosine of each element in a_1:", np.cos(a_1))
print("Tangent of each element in a_1:", np.tan(a_1))
print("Hyperbolic sine of each element in a_1:", np.sinh(a_1))
print("Hyperbolic cosine of each element in a_1:", np.cosh(a_1))
print("Hyperbolic tangent of each element in a_1:", np.tanh(a_1))
print("Rounding each element in a_1 to the nearest integer:", np.round(a_1))
print("Floor of each element in a_1 (rounding down):", np.floor(a_1))
print("Ceiling of each element in a_1 (rounding up):", np.ceil(a_1))
print("Absolute value of each element in a_1:", np.abs(a_1))
print("Maximum value in a_1:", np.max(a_1))
print("Minimum value in a_1:", np.min(a_1))
print("Sum of all elements in a_1:", np.sum(a_1))