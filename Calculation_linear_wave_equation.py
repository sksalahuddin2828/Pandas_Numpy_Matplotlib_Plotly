import sympy as sp

# Define symbols
x, t = sp.symbols('x t')
v = sp.symbols('v', positive=True)  # Wave speed

# Define the given wave equation
y = 0.50 * sp.cos(0.20 * sp.pi * (-1) * x - 4.00 * sp.pi * (-1) * t + sp.pi / 10)

# Calculate second partial derivatives
partial2_y_x2 = sp.diff(y, x, x)
partial2_y_t2 = sp.diff(y, t, t)

# Check if the wave equation satisfies the linear wave equation
is_linear_wave = sp.simplify(partial2_y_x2 / (1 / v**2) - partial2_y_t2)

if is_linear_wave == 0:
    print("The given wave equation satisfies the linear wave equation.")
else:
    print("The given wave equation does not satisfy the linear wave equation.")


# Answer: The given wave equation does not satisfy the linear wave equation.
