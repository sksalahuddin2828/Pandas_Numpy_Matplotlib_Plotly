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

# Create a colormap for coloring the muon path based on time
colors = cm.jet(np.linspace(0, 1, len(x)))

# Create scatter plot for high-energy interactions
scatter = ax.scatter([], [], [], color='red', alpha=0.8, s=80, label='Muon Creation')

# Create line plot for muon path
line, = ax.plot([], [], [], color='blue', lw=2, label='Muon Path')

def update(frame):
    scatter.set_offsets(np.array([[x[frame], y[frame], z[frame]]]))
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    scatter.set_color(colors[frame])
    return scatter, line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x), interval=10, blit=True)

# Add title and labels
ax.set_title('Muon Paradox Simulation')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

# Create colorbar legend
sm = plt.cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(vmin=0, vmax=len(x)))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, label='Time Step')

# Add legend
ax.legend(loc='upper right')

# Display the animation
plt.show()
