import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib import cm

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

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Create scatter plot for muon creation
scatter_creation = ax.scatter([], [], [], color='red', alpha=0.8, s=80, label='Muon Creation')

# Create scatter plot for muon path
scatter_path = ax.scatter([], [], [], c=[], cmap='jet', alpha=0.8, s=20, label='Muon Path')

def update(frame):
    scatter_creation.set_offsets(np.array([[x[0], y[0], z[0]]]))
    scatter_path.set_offsets(np.array([[x[frame], y[frame], z[frame]]]))
    scatter_path.set_array(np.array(range(frame)))  # Use frame as color array
    return scatter_creation, scatter_path

# Create animation
ani = FuncAnimation(fig, update, frames=len(x), interval=10, blit=True)

# Add title and labels
ax.set_title('Muon Paradox Simulation')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

# Add colorbar
cbar = plt.colorbar(scatter_path, ax=ax, label='Time Step')

# Add legend
ax.legend(loc='upper right')

# Display the animation
plt.show()
