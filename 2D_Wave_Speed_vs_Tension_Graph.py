import numpy as np
import matplotlib.pyplot as plt

# Range of tension values
tension_range = np.linspace(1, 200, 100)

# Calculate wave speeds for each tension value
wave_speed_values = [wave_speed_equation.subs([(FT, T), (mu, linear_density_value)]) for T in tension_range]

# Create a plot
plt.figure()
plt.plot(tension_range, wave_speed_values)
plt.xlabel('Tension (FT)')
plt.ylabel('Wave Speed (v)')
plt.title('Wave Speed vs Tension')
plt.grid()
plt.show()
