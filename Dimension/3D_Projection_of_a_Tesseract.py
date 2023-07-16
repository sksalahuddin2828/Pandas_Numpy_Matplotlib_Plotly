import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define tesseract vertices
vertices = np.array([
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1],
    [-1, -1, -1, 1, -1],
    [-1, -1, -1, 1, 1],
    [-1, -1, 1, -1, -1],
    [-1, -1, 1, -1, 1],
    [-1, -1, 1, 1, -1],
    [-1, -1, 1, 1, 1],
    [-1, 1, -1, -1, -1],
    [-1, 1, -1, -1, 1],
    [-1, 1, -1, 1, -1],
    [-1, 1, -1, 1, 1],
    [-1, 1, 1, -1, -1],
    [-1, 1, 1, -1, 1],
    [-1, 1, 1, 1, -1],
    [-1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]  # Second dimension vertex
])


# Define edges of the tesseract
edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7),
         (4, 5), (4, 6), (5, 7), (6, 7), (8, 9), (8, 10), (8, 12), (9, 11),
         (9, 13), (10, 11), (10, 14), (11, 15), (12, 13), (12, 14), (13, 15),
         (14, 15), (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14),
         (7, 15)]

# Create a figure and axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.axis('off')

# Project vertices onto 3D space (select the first three components)
projected_vertices = vertices[:, :3]

# Plot the tesseract edges
for edge in edges:
    ax.plot3D(*zip(projected_vertices[edge[0]], projected_vertices[edge[1]]), color='gray', linestyle='dashed', linewidth=1)

# Plot projected vertices with labels
for i, vertex in enumerate(projected_vertices):
    ax.text(*vertex, s=str(i), fontsize=8, ha='center', va='center')

# Create illusion lines connecting projected vertices
for i in range(len(projected_vertices)):
    for j in range(i+1, len(projected_vertices)):
        ax.plot([projected_vertices[i, 0], projected_vertices[j, 0]],
                [projected_vertices[i, 1], projected_vertices[j, 1]],
                [projected_vertices[i, 2], projected_vertices[j, 2]], 'k--', alpha=0.3)

# Add a title and description
ax.set_title('3D Projection of a Tesseract (4D Hypercube)')
ax.text2D(0.05, 0.95, 'A tesseract is a 4D hypercube represented in 3D space using projection.\n'
                      'The color coding represents the 5th dimension.', transform=ax.transAxes, fontsize=10)

# Display the plot
plt.show()
