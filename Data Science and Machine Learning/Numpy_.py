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



