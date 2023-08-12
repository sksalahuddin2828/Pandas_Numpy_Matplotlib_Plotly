import numpy as np

# Given matrix
A = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])

# Check if the matrix is symmetric
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)

if is_symmetric(A):
    print("Matrix A is symmetric.")
else:
    print("Matrix A is not symmetric.")


# Answer: Matrix A is symmetric.
