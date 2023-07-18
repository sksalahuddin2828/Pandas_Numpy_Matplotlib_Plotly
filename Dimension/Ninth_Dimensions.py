import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_hypercube_vertices(dimensions):
    vertices = np.array(np.meshgrid(*([-1, 1],) * dimensions)).T.reshape(-1, dimensions)
    return vertices

def generate_hypercube_edges(dimensions):
    vertices = generate_hypercube_vertices(dimensions)
    edges = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if np.sum(vertices[i] != vertices[j]) == 1:
                edges.append((i, j))
    return edges

# Define the number of dimensions for the hypercube
num_dimensions = 9

# Generate hypercube vertices and edges
vertices = generate_hypercube_vertices(num_dimensions)
edges = generate_hypercube_edges(num_dimensions)

# Create a figure and axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.axis('off')

# Plot the 9D hypercube edges
for edge in edges:
    ax.plot3D(*zip(vertices[edge[0]][:3], vertices[edge[1]][:3]), color='black')
    ax.plot3D(*zip(vertices[edge[0]][3:6], vertices[edge[1]][3:6]), color='black')
    ax.plot3D(*zip(vertices[edge[0]][6:9], vertices[edge[1]][6:9]), color='black')

# Define rotation matrix for the first three dimensions
angle = np.pi / 4
rotation_matrix_3d = np.array([[np.cos(angle), 0, -np.sin(angle)],
                               [0, np.cos(angle), 0],
                               [np.sin(angle), 0, np.cos(angle)]])

# Project vertices onto 3D space
projected_vertices_3d = np.dot(vertices[:, :3], rotation_matrix_3d)

# Define rotation matrix for the fourth, fifth, sixth, seventh, and eighth dimensions
rotation_matrix_45678 = np.array([[1, 0, 0],
                                  [0, np.cos(angle), -np.sin(angle)],
                                  [0, np.sin(angle), np.cos(angle)]])

# Project vertices from 3D space to the fourth, fifth, sixth, seventh, and eighth dimensions
projected_vertices_45678 = np.dot(projected_vertices_3d, rotation_matrix_45678)

# Define rotation matrix for the ninth dimension
rotation_matrix_9 = np.array([[np.cos(angle), -np.sin(angle), 0],
                              [np.sin(angle), np.cos(angle), 0],
                              [0, 0, 1]])

# Project vertices from 8D space to the ninth dimension
projected_vertices_9 = np.dot(projected_vertices_45678, rotation_matrix_9)

# Plot projected vertices with labels
labels = [''.join(str(v) for v in vertex) for vertex in vertices]
sc = ax.scatter(projected_vertices_3d[:, 0], projected_vertices_3d[:, 1], projected_vertices_3d[:, 2],
                s=100, c=projected_vertices_9[:, 2], cmap='viridis')
for i, label in enumerate(labels):
    ax.text(projected_vertices_3d[i, 0], projected_vertices_3d[i, 1], projected_vertices_3d[i, 2],
            label, fontsize=8, ha='center', va='center')

# Create illusion lines connecting projected vertices in 3D space
for i in range(len(projected_vertices_3d)):
    for j in range(i + 1, len(projected_vertices_3d)):
        ax.plot([projected_vertices_3d[i, 0], projected_vertices_3d[j, 0]],
                [projected_vertices_3d[i, 1], projected_vertices_3d[j, 1]],
                [projected_vertices_3d[i, 2], projected_vertices_3d[j, 2]], 'k--', alpha=0.3)

# Add a color bar for the ninth dimension
cbar = fig.colorbar(sc, ax=ax, shrink=0.8)
cbar.set_label('Ninth Dimension')

# Display the plot
plt.show()
