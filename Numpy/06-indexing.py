import numpy as np

# 1D Array (One-dimensional)
arr_1d = np.array([10, 20, 30, 40, 50])

# 2D Array (Two-dimensional)
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

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

print(arr_1d[0])
print(arr_2d[1][2])
print(arr_3d[0][1][1])