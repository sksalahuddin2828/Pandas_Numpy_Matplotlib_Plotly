import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

r = sp.symbols('r')
recurrence_relation = 2*r**2 - 5*r + 2

roots = sp.solve(recurrence_relation, r)
print("Roots of the characteristic equation:", roots)

C1, C2 = sp.symbols('C1 C2')
a0_condition = C1 + C2
a1_condition = C1 + 2*C2

# Solve for C1 and C2
C1_value, C2_value = sp.solve([a0_condition - 0, a1_condition - 1], (C1, C2))

particular_solution = C1_value * roots[0]**r + C2_value * roots[1]**r
print("Particular solution:", particular_solution)
