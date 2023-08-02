import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Define the symbolic variable 'r' and the recurrence relation
r = sp.symbols('r')
recurrence_relation = r**2 - 3*r + 2

# Solve the characteristic equation for the roots (values of 'r')
roots = sp.solve(recurrence_relation, r)
print("Roots of the equation:", roots)

# Define the homogeneous solution of the difference equation
homogeneous_solution = [sp.Symbol(f'C{i}') * r**i for i in range(len(roots))]

print("Homogeneous Solution:")
for i, solution in enumerate(homogeneous_solution):
    print(f"yK = {solution}")

# Define the symbolic variable 'K' and the recurrence relation
K = sp.symbols('K')
recurrence_relation = 9*K**2 - 6*K + 1

# Solve the characteristic equation for the roots (values of 'K')
roots = sp.solve(recurrence_relation, K)
print("Roots of the equation:", roots)

# Define the homogeneous solution of the difference equation
homogeneous_solution = [sp.Symbol(f'A{i}') * K**i for i in range(len(roots))]

print("Homogeneous Solution:")
for i, solution in enumerate(homogeneous_solution):
    print(f"yK = {solution}")

# Define the symbolic variable 'K' and the recurrence relation
K = sp.symbols('K')
recurrence_relation = K**2 - K - 1

# Solve the characteristic equation for the roots (values of 'K')
roots = sp.solve(recurrence_relation, K)
print("Roots of the equation:", roots)

# Define the homogeneous solution of the difference equation
homogeneous_solution = [sp.Symbol(f'X{i}') * K**i for i in range(len(roots))]

print("Homogeneous Solution:")
for i, solution in enumerate(homogeneous_solution):
    print(f"yK = {solution}")

# Define the symbolic variable 'K' and the recurrence relation
K = sp.symbols('K')
recurrence_relation = K**4 + 4*K**3 + 8*K**2 + 8*K + 4

# Solve the characteristic equation for the roots (values of 'K')
roots = sp.solve(recurrence_relation, K)
print("Roots of the equation:", roots)

# Define the homogeneous solution of the difference equation
homogeneous_solution = [sp.Symbol(f'Z{i}') * K**i for i in range(len(roots))]

print("Homogeneous Solution:")
for i, solution in enumerate(homogeneous_solution):
    print(f"yK = {solution}")



# Answer: Roots of the equation: [1, 2]
#         Homogeneous Solution:
#         yK = C0
#         yK = C1*r
#         Roots of the equation: [1/3]
#         Homogeneous Solution:
#         yK = A0
#         Roots of the equation: [1/2 - sqrt(5)/2, 1/2 + sqrt(5)/2]
#         Homogeneous Solution:
#         yK = X0
#         yK = K*X1
#         Roots of the equation: [-1 - I, -1 + I]
#         Homogeneous Solution:
#         yK = Z0
#         yK = K*Z1
