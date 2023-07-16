import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
import numpy as np

# Define the vertices of the tesseract
vertices = np.array([
    [-1, -1, -1, -1],
    [-1, -1, -1, 1],
    [-1, -1, 1, -1],
    [-1, -1, 1, 1],
    [-1, 1, -1, -1],
    [-1, 1, -1, 1],
    [-1, 1, 1, -1],
    [-1, 1, 1, 1],
    [1, -1, -1, -1],
    [1, -1, -1, 1],
    [1, -1, 1, -1],
    [1, -1, 1, 1],
    [1, 1, -1, -1],
    [1, 1, -1, 1],
    [1, 1, 1, -1],
    [1, 1, 1, 1]
])

# Define the edges of the tesseract
edges = [
    [0, 1], [0, 2], [0, 4], [1, 3], [1, 5], [2, 3], [2, 6], [3, 7],
    [4, 5], [4, 6], [5, 7], [6, 7], [8, 9], [8, 10], [8, 12], [9, 11],
    [9, 13], [10, 11], [10, 14], [11, 15], [12, 13], [12, 14], [13, 15], [14, 15],
    [0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]
]

# Generate the initial 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Store the lines of the tesseract
lines = [ax.plot(vertices[edge, 0], vertices[edge, 1], vertices[edge, 2], 'k')[0] for edge in edges]

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Function to update the rotation
def update_rotation(frame):
    ax.view_init(elev=10, azim=frame * 2)
    return lines

# Create the animation
animation = FuncAnimation(fig, update_rotation, frames=180, interval=50, blit=True)

plt.show()

