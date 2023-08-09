# Step 1: Import Required Libraries
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Constants and Variables
FT = sp.symbols('FT')  # Tension in the string
mu = sp.symbols('mu')  # Linear density
v = sp.symbols('v')    # Wave speed

# Step 2: Derive the Equation for Wave Speed
# Derive the equation using the given equation and algebraic manipulation
equation = sp.Eq(1 / v**2, mu * FT)
wave_speed_equation = sp.solve(equation, v)[0]

# Step 3 and 4: Define Constants and Calculate Wave Speed
# Define values for tension and linear density
tension_value = 10.0  # Example value for tension (replace with your value)
linear_density_value = 0.05  # Example value for linear density (replace with your value)

# Substitute values into the equation
wave_speed_value = wave_speed_equation.subs([(FT, tension_value), (mu, linear_density_value)])

print("Calculated Wave Speed:", wave_speed_value)

# Step 5: Visualization
tension_range = np.linspace(1, 20, 100)  # Range of tension values
wave_speed_values = [wave_speed_equation.subs([(FT, T), (mu, linear_density_value)]) for T in tension_range]

# Create a plot
plt.figure()
plt.plot(tension_range, wave_speed_values, label='Wave Speed vs Tension')
plt.xlabel('Tension')
plt.ylabel('Wave Speed')
plt.title('Wave Speed vs Tension')
plt.legend()
plt.grid()
plt.show()
