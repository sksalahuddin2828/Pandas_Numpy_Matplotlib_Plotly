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

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
line, = ax.plot([], [], [], color='b', lw=2)

def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x), interval=10, blit=True)

# Display the animation
plt.show()
