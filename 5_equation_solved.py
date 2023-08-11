import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Example 2: Solve 3x^2 - 5x + 2 = 0
x = sp.symbols('x')
equation = 3*x**2 - 5*x + 2
solutions = sp.solve(equation, x)
print("Example 2 Solutions:", solutions)

# Example 3: Solve 3x + 9 = 2x + 18
equation = 3*x + 9 - (2*x + 18)
solution = sp.solve(equation, x)
print("Example 3 Solution:", solution[0])

# Example 4: Solve x + 2y = 1 and x = y
y = sp.symbols('y')
equation1 = x + 2*y - 1
equation2 = x - y
solutions = sp.solve([equation1, equation2], (x, y))
print("Example 4 Solutions:", solutions)

# Example 5: Solve x = 12(x + 2)
equation = x - 12*(x + 2)
solution = sp.solve(equation, x)
print("Example 5 Solution:", solution[0])

# Example 6: Solve 7x + 21 = 6x + 26
equation = 7*x + 21 - (6*x + 26)
solution = sp.solve(equation, x)
print("Example 6 Solution:", solution[0])


# Answer: Example 2 Solutions: [2/3, 1]
#         Example 3 Solution: 9
#         Example 4 Solutions: {x: 1/3, y: 1/3}
#         Example 5 Solution: -24/11
#         Example 6 Solution: 5
