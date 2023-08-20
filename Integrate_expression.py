import sympy as sp

# Define the variable and constant
x, a = sp.symbols('x a')
c = sp.Symbol('c')  # Constant of integration

# Define the expression
expression = sp.exp(a * x)

# Integrate the expression
integral_result = sp.integrate(expression, x) + c

print(integral_result)


# Answer: c + Piecewise((exp(a*x)/a, Ne(a, 0)), (x, True))
