import sympy as sp

# Define variables and equations
x, y = sp.symbols('x y')
eq1 = 4*x + 5*y - 19
eq2 = 5*x - y/2 - 2

# Solve equations
sol = sp.solve((eq1, eq2), (x, y))
print("Solution:", sol)


# Answer: Solution: {x: 13/18, y: 29/9}
