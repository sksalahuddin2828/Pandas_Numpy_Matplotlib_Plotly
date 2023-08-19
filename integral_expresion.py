import sympy as sp

x = sp.symbols('x')
integral_expr = sp.integrate(sp.sin(x), x)

print(integral_expr)

# Answer: -cos(x)
