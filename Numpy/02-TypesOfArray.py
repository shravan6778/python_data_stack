import numpy as np

# 1D Array (One-dimensional)
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)
print("Dimensions:", arr_1d.ndim)
print()

# 2D Array (Two-dimensional)
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Dimensions:", arr_2d.ndim)
print()

# 3D Array (Three-dimensional)
arr_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])
print("3D Array:")
print(arr_3d)
print("Shape:", arr_3d.shape)
print("Dimensions:", arr_3d.ndim)
print()

# Accessing elements
print("Accessing elements:")
print("1D -> Element at index 2:", arr_1d[2])
print("2D -> Element at row 1, col 2:", arr_2d[1][2])
print("3D -> Element at block 1, row 0, col 1:", arr_3d[1][0][1])
