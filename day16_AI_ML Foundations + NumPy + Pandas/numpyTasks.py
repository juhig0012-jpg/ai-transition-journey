import numpy as np

# Create a 3x3 matrix
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Find matrix sum
matrix_sum = matrix1 + matrix2
print("\nMatrix Sum:")
print(matrix_sum)

# Find average of all elements in matrix1
average = np.mean(matrix1)
print("\nAverage of Matrix 1:", average)

# Reshape array
array = np.arange(1, 13)  # 1 to 12
reshaped_array = array.reshape(3, 4)

print("\nOriginal Array:")
print(array)

print("\nReshaped Array (3x4):")
print(reshaped_array)

# Generate random numbers
random_numbers = np.random.randint(1, 100, size=(3, 3))

print("\nRandom 3x3 Matrix:")
print(random_numbers)