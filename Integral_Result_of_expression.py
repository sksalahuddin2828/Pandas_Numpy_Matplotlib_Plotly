import sympy as sp

# Define symbolic variables
x, a = sp.symbols('x a')

# Define the expression and integrate
expression = a**2 + x**2
integral_result = sp.integrate(expression, x)
print("Integral Result:", integral_result)


# Answer: Integral Result: a**2*x + x**3/3
