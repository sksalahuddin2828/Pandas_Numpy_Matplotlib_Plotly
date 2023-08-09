import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp

# Constants and Variables
FT = sp.symbols('FT')  # Tension in the string
mu = sp.symbols('mu')  # Linear density
v = sp.symbols('v')    # Wave speed

# Derive the Equation for Wave Speed
equation = sp.Eq(1 / v**2, mu * FT)
wave_speed_equation = sp.solve(equation, v)[0]

# Define values for linear density
linear_density_value = 0.05

# Visualization
tension_range = np.linspace(1, 20, 100)  # Range of tension values
wave_speed_values = [wave_speed_equation.subs([(FT, T), (mu, linear_density_value)]) for T in tension_range]

fig, ax = plt.subplots()
line, = ax.plot(tension_range, wave_speed_values, label='Wave Speed vs Tension')
ax.set_xlabel('Tension')
ax.set_ylabel('Wave Speed')
ax.set_title('Wave Speed vs Tension')
ax.legend()
ax.grid()

# Animation function
def animate(frame):
    line.set_data(tension_range[:frame], wave_speed_values[:frame])

# Create animation
ani = FuncAnimation(fig, animate, frames=len(tension_range), interval=100, blit=False)

# Show animation
plt.show()
