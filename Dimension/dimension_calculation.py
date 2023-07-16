import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.text import Annotation

# Define tesseract vertices
vertices = np.array([[-1, -1, -1, -1],
                     [-1, -1, -1,  1],
                     [-1, -1,  1, -1],
                     [-1, -1,  1,  1],
                     [-1,  1, -1, -1],
                     [-1,  1, -1,  1],
                     [-1,  1,  1, -1],
                     [-1,  1,  1,  1],
                     [ 1, -1, -1, -1],
                     [ 1, -1, -1,  1],
                     [ 1, -1,  1, -1],
                     [ 1, -1,  1,  1],
                     [ 1,  1, -1, -1],
                     [ 1,  1, -1,  1],
                     [ 1,  1,  1, -1],
                     [ 1,  1,  1,  1]])

# Define edges of the tesseract
edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7),
         (4, 5), (4, 6), (5, 7), (6, 7), (8, 9), (8, 10), (8, 12), (9, 11),
         (9, 13), (10, 11), (10, 14), (11, 15), (12, 13), (12, 14), (13, 15),
         (14, 15), (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14),
         (7, 15)]

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')

# Plot the tesseract with enhanced features
edge_lines = []
for edge in edges:
    line = ax.plot3D(*zip(vertices[edge[0]], vertices[edge[1]]), color='black', alpha=0.4, linewidth=1)
    edge_lines.append(line)

vertex_labels = [''.join(str(v) for v in vertex) for vertex in vertices]
for i, vertex in enumerate(vertices):
    x, y, z, _ = vertex
    ax.text(x, y, z, vertex_labels[i], fontsize=8, ha='center', va='center')

# Set initial view
ax.view_init(elev=20, azim=45)

# Function to update the plot for animation
def update_plot(frame):
    ax.cla()  # Clear previous frame
    ax.set_aspect('auto')

    # Rotate the tesseract
    rotation_matrix = np.array([[np.cos(frame), -np.sin(frame)],
                                [np.sin(frame), np.cos(frame)]])
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Plot the rotated tesseract with enhanced features
    for i, edge in enumerate(edges):
        line = ax.plot3D(*zip(rotated_vertices[edge[0]], rotated_vertices[edge[1]]),
                         color=plt.cm.viridis(frame / (2 * np.pi)), linewidth=2)
        edge_lines[i] = line

    # Scale the plot dynamically
    ax.auto_scale_xyz([-3, 3], [-3, 3], [-3, 3])

    # Add annotations
    for i, vertex in enumerate(rotated_vertices):
        x, y, z, _ = vertex
        annotation = Annotation(vertex_labels[i], (x, y, z), xytext=(0, -10), textcoords='offset points',
                                ha='center', va='center', fontsize=8, color='red')
        ax.add_artist(annotation)

    # Set new view
    ax.view_init(elev=20, azim=45 + frame * 180 / np.pi)

# Animate the plot
frames = np.linspace(0, 2 * np.pi, 100)
animation = FuncAnimation(fig, update_plot, frames=frames, interval=100)

# Display the animation
plt.show()
