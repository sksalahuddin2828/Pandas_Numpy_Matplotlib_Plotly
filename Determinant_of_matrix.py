import numpy as np
import sympy as sp

# Example of solving equations
x = sp.Symbol('x')
equation = sp.Eq(x**2 - 4*x + 4, 0)
solution = sp.solve(equation, x)
print("Solution:", solution)

# Other mathematical computations
a = np.array([[1, 2], [3, 4]])
det_a = np.linalg.det(a)
print("Determinant of matrix a:", det_a)


# Answer: Solution: [2]
#         Determinant of matrix a: -2.0000000000000004
