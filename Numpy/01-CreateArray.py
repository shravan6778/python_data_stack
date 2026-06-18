"""
NumPy (short for Numerical Python) is a popular Python library used for scientific computing, numerical calculations, and data analysis.

Why is NumPy used?
1. Fast numerical computations
NumPy stores data in efficient arrays and performs operations much faster than standard Python lists.

2. Powerful N-dimensional arrays
The core object in NumPy is the ndarray (N-dimensional array), which can represent:
1D arrays (vectors)
2D arrays (matrices)
3D and higher-dimensional data

3. Mathematical operations
NumPy provides built-in functions for:
Mean
Median
Standard deviation
Trigonometric functions
Linear algebra

4. Supports vectorization
Operations are applied to entire arrays without loops, making code shorter and faster.

5. Foundation for other libraries
Many Python libraries for data science and machine learning are built on NumPy, including:
Pandas
SciPy
Scikit-learn
TensorFlow
PyTorch

creattion of arrays in python
To convert the list into array we use array() method 
"""

import numpy as np 
arr = np.array([1,2,3,4,5])
print(arr)

#create an array with all default values as zeros
arr_zeros_1d= np.zeros(3)
arr_zeros_2d=np.zeros((2,3))
print(f"Array with zeros for\n 1D:{arr_zeros_1d}\n 2D : {arr_zeros_2d}")

#create an array with all default values as ones
arr_ones_1d= np.ones(3)
arr_ones_2d=np.ones((2,3))
print(f"Array with ones for\n 1D:{arr_ones_1d}\n 2D : {arr_ones_2d}")

#create an array with all default values with any specific number
arr_sp_1d= np.full(12,10)
arr_sp_2d=np.full((2,3),7)
print(f"Array with any specific value for\n 1D:{arr_sp_1d}\n 2D : {arr_sp_2d}")

#create an array to generate and store sequences of numbers with arrange() method
arr_arrange=np.arange(1,20,2)
print(f"Arrange method array : {arr_arrange}")

# To create an identity matrices use eye() method 
arr_iden=np.eye(3)
print(f"Identity Matrix :\n {arr_iden}")