import numpy as np

# 1D Array (One-dimensional)
arr_1d = np.array([10, 20, 30, 40, 50, 60])

print(arr_1d[0:4])
print(arr_1d[2:4:1])
print(arr_1d[:5])
print(arr_1d[::2])
print(arr_1d[::-1])

# Funny index -- Selecting multiple elements at once
print(arr_1d[[1,3,5]])

# Boolean Masking -- Selecting the elements based on condition
print(arr_1d[arr_1d>30])
