import numpy as np
import pandas as pd
import sympy as sp

# Define the universe U and create a pandas DataFrame for propositions
U = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
df = pd.DataFrame({'x': U})

# Define the proposition p(x) and evaluate it for each value of x
x = sp.Symbol('x')
p = x**2 - 4
df['p(x)'] = df['x'].apply(lambda val: p.subs(x, val))

print(df)


# Answer:     x p(x)
#         0  -5   21
#         1  -4   12
#         2  -3    5
#         3  -2    0
#         4  -1   -3
#         5   0   -4
#         6   1   -3
#         7   2    0
#         8   3    5
#         9   4   12
#         10  5   21
