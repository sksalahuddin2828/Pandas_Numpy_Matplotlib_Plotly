import sympy as sp

# Define the symbol and variable
x = sp.symbols('x')
m = sp.symbols('m')

# Define the integral expression
integral_expr = x**m

# Calculate the indefinite integral
indefinite_integral = sp.integrate(integral_expr, x)

# Print the indefinite integral
print("Indefinite Integral:", indefinite_integral)


# Answer: Indefinite Integral: Piecewise((x**(m + 1)/(m + 1), Ne(m, -1)), (log(x), True))
