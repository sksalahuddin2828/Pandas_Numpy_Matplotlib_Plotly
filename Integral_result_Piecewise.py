import sympy as sp

# Define symbolic variables
x, a = sp.symbols('x a')

# Define the expression
expression = x * sp.exp(a * x)

# Integrate the expression
integral_result = sp.integrate(expression, x)

# Print the integral result
print("Integral result:", integral_result)

# Answer: Integral result: Piecewise(((a*x - 1)*exp(a*x)/a**2, Ne(a**2, 0)), (x**2/2, True))
