import numpy as np
import sympy as sp

# Define symbols
a, b, c, gamma = sp.symbols('a b c gamma')

# Define the Law of Cosines equation
law_of_cosines_eq = sp.Eq(c**2, a**2 + b**2 - 2 * a * b * sp.cos(gamma))

# Solve for c
solution_c = sp.solve(law_of_cosines_eq, c)[0]
print("Solution for c:", solution_c)


# Answer: Solution for c: -sqrt(a**2 - 2*a*b*cos(gamma) + b**2)
