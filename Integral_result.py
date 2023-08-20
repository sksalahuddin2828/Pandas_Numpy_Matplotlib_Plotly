import sympy as sp

# Define variables
x, a = sp.symbols('x a')

# Define the expression
expression = sp.sin(a * x) * sp.cos(a * x)

# Perform integration
integral_result = sp.integrate(expression, x)

print(integral_result)

# Answer: Piecewise((sin(a*x)**2/(2*a), Ne(a, 0)), (0, True))
