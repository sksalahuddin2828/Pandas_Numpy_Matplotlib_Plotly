import sympy as sp

# Define symbols
v, FT, mu = sp.symbols('v FT mu')

# Wave speed equation
wave_speed_equation = sp.sqrt(FT / mu)

# Print the derived equation
print("Derived Wave Speed Equation:", wave_speed_equation)

# Given values
tension_value = 100.0  # Example value for tension (replace with your value)
linear_density_value = 0.01  # Example value for linear density (replace with your value)

# Substitute values into the equation
calculated_wave_speed = wave_speed_equation.subs([(FT, tension_value), (mu, linear_density_value)])

print("Calculated Wave Speed:", calculated_wave_speed)


# Answer: Derived Wave Speed Equation: sqrt(FT/mu)
#         Calculated Wave Speed: 100.000000000000
