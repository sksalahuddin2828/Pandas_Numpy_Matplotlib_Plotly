import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbols
alpha, beta = sp.symbols('alpha beta')

# Define the identity
lhs = sp.cos(alpha + beta)
rhs = sp.cos(alpha) * sp.cos(beta) - sp.sin(alpha) * sp.sin(beta)

# Check if the identity holds true
identity_holds = sp.simplify(lhs - rhs) == 0
print("Does the identity hold true?", identity_holds)

# Create 3D plot for visualization
alpha_vals = np.linspace(0, 2 * np.pi, 100)
beta_vals = np.linspace(0, 2 * np.pi, 100)
alpha_vals, beta_vals = np.meshgrid(alpha_vals, beta_vals)

lhs_vals = np.cos(alpha_vals + beta_vals)
rhs_vals = np.cos(alpha_vals) * np.cos(beta_vals) - np.sin(alpha_vals) * np.sin(beta_vals)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(alpha_vals, beta_vals, lhs_vals, cmap='coolwarm', label='lhs')
ax.plot_surface(alpha_vals, beta_vals, rhs_vals, cmap='viridis', label='rhs')

ax.set_xlabel('Alpha')
ax.set_ylabel('Beta')
ax.set_zlabel('Value')
ax.set_title('Trigonometric Identity: cos(α±β) = cosαcosβ ∓ sinαsinβ')

from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.cla()  # Clear the previous frame
    new_alpha = alpha_vals + frame * 0.1
    new_lhs = np.cos(new_alpha + beta_vals)
    new_rhs = np.cos(new_alpha) * np.cos(beta_vals) - np.sin(new_alpha) * np.sin(beta_vals)
    ax.plot_surface(alpha_vals, beta_vals, new_lhs, cmap='coolwarm', label='lhs')
    ax.plot_surface(alpha_vals, beta_vals, new_rhs, cmap='viridis', label='rhs')
    ax.set_xlabel('Alpha')
    ax.set_ylabel('Beta')
    ax.set_zlabel('Value')
    ax.set_title('Trigonometric Identity Animation')
    ax.legend()

ani = FuncAnimation(fig, update, frames=50, interval=100)
plt.show()
