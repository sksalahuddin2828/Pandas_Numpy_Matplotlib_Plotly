import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Constants
A = 1.0
k = 2.0
ω = 3.0

x = np.linspace(0, 10, 100)
t = np.linspace(0, 5, 50)
X, T = np.meshgrid(x, t)

# Calculate wave functions
y1 = A * np.sin(k * X - ω * T)
y2 = A * np.sin(2 * k * X + 2 * ω * T)
yR = y1 + y2

# Create 3D subplots for individual waves and resulting wave
fig = plt.figure()
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

ax1.plot_surface(X, T, y1, cmap='viridis')
ax2.plot_surface(X, T, y2, cmap='plasma')
ax3.plot_surface(X, T, yR, cmap='inferno')

plt.show()

# Calculate partial derivatives
partial_yR_x = A * k * np.cos(k * X - ω * T) + 2 * A * k * np.cos(2 * k * X + 2 * ω * T)
partial2_yR_x2 = -A * k*2 * np.sin(k * X - ω * T) - 4 * A * k*2 * np.sin(2 * k * X + 2 * ω * T)
partial_yR_t = -A * ω * np.sin(k * X - ω * T) + 2 * A * ω * np.sin(2 * k * X + 2 * ω * T)
partial2_yR_t2 = -A * ω*2 * np.sin(k * X - ω * T) - 4 * A * ω*2 * np.sin(2 * k * X + 2 * ω * T)

# Calculate velocity of resulting wave using the wave equation
v_resulting = ω / k

# Display velocity
print(f"Velocity of resulting wave: {v_resulting}")

# Create a Plotly surface plot for the resulting wave velocity
fig = go.Figure(data=[
    go.Surface(x=X, y=T, z=partial2_yR_x2 / (partial2_yR_t2 / v_resulting**2), colorscale='plasma')
])

# Update z-axis layout with tick suffix
fig.update_layout(scene=dict(zaxis=dict(ticksuffix=' units')))
fig.update_layout(title='Velocity of Resulting Wave in 3D')
fig.show()
