import sympy as sp

# Define symbols
v, FT, mu = sp.symbols('v FT mu')

# Wave speed equation
wave_speed_equation = sp.sqrt(FT / mu)

# Print the derived equation
print("Derived Wave Speed Equation:", wave_speed_equation)
