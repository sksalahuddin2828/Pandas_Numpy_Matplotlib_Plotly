import sympy as sp

# Define symbols
x, y, z = sp.symbols('x y z')

# Express mathematical equations
equation_1 = x**2 + y**2
equation_2 = sp.sin(x) + sp.cos(y)

# Simplify equations
simplified_equation_1 = sp.simplify(equation_1)
simplified_equation_2 = sp.simplify(equation_2)

# Print the results
print("Equation 1:", equation_1)
print("Simplified Equation 1:", simplified_equation_1)
print("Equation 2:", equation_2)
print("Simplified Equation 2:", simplified_equation_2)


# Answer: Equation 1: x**2 + y**2
#         Simplified Equation 1: x**2 + y**2
#         Equation 2: sin(x) + cos(y)
#         Simplified Equation 2: sin(x) + cos(y)
