import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
from mpl_toolkits.mplot3d import Axes3D

# Define a symbolic variable
x = sp.Symbol('x')

# Solve equation: 3x + 5 = 12
equation = sp.Eq(3*x + 5, 12)
solution = sp.solve(equation, x)

print("Symbolic Solution:")
print(solution)

# Define the function
def quadratic_function(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Function: ax^2 + bx + c')

# Create interactive widget
interact(quadratic_function, a=(-2, 2, 0.1), b=(-5, 5, 0.1), c=(-10, 10, 0.1))

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate random data
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

ax.scatter(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Interactive 3D Scatter Plot')

plt.show()

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)

print("Matrix C:")
print(C)
