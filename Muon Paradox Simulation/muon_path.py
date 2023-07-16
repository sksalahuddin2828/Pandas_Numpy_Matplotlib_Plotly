import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def calculate_muon_path(v, t, dt):
    x = []
    y = []
    z = []
    gamma = 1 / np.sqrt(1 - v**2)
    t_prime = gamma * t

    while t >= 0:
        x.append(v * t)
        y.append(0)
        z.append(0)
        t -= dt

    return x, y, z

# Parameters
v = 0.99  # Velocity of muon (as a fraction of the speed of light)
t = 2e-6  # Proper time experienced by the muon (in seconds)
dt = 1e-7  # Time step for simulation (in seconds)

# Calculate muon path
x, y, z = calculate_muon_path(v, t, dt)

# Determine plot limits
max_range = np.max([np.abs(x), np.abs(y), np.abs(z)])
limit = 1.1 * max_range

# Create 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

# Create scatter plot for muon creation
ax.scatter([x[0]], [y[0]], [z[0]], color='red', alpha=0.8, s=80, label='Muon Creation')

# Create line plot for muon path
ax.plot(x, y, z, color='blue', alpha=0.8, lw=2, label='Muon Path')

# Add title and labels
ax.set_title('Muon Paradox Simulation')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

# Add legend
ax.legend(loc='upper right')

# Display the plot
plt.show()
