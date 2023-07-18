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
num_dimensions = 10

# Generate hypercube vertices and edges
vertices = generate_hypercube_vertices(num_dimensions)
edges = generate_hypercube_edges(num_dimensions)

# Create a figure and axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.axis('off')

# Plot the 10D hypercube edges
for edge in edges:
    ax.plot3D(*zip(vertices[edge[0]][:3], vertices[edge[1]][:3]), color='black', alpha=0.4)
    ax.plot3D(*zip(vertices[edge[0]][3:6], vertices[edge[1]][3:6]), color='black', alpha=0.4)
    ax.plot3D(*zip(vertices[edge[0]][6:9], vertices[edge[1]][6:9]), color='black', alpha=0.4)
    ax.plot3D([vertices[edge[0]][9]], [vertices[edge[1]][9]], [0], color='black', alpha=0.4)

# Define rotation matrices for different dimensions
angles = np.linspace(0, 2 * np.pi, num_dimensions + 1)[:-1]
rotation_matrices = [np.array([[np.cos(angle), -np.sin(angle), 0],
                               [np.sin(angle), np.cos(angle), 0],
                               [0, 0, 1]])
                     for angle in angles]

# Apply rotations to the vertices
projected_vertices = vertices[:, :3]
for i in range(3, num_dimensions):
    projected_vertices = np.dot(projected_vertices, rotation_matrices[i])

# Define a fractal function for the tenth dimension
def fractal_function(x, y, z):
    return np.sin(x) * np.cos(y) * np.sin(z)

# Define the recursion depth for the fractal pattern
recursion_depth = 5

# Apply the fractal function recursively to the tenth dimension
def apply_fractal_function(x, y, z, depth):
    if depth == 0:
        return fractal_function(x, y, z)
    else:
        return apply_fractal_function(fractal_function(x, y, z), fractal_function(y, z, x), fractal_function(z, x, y), depth - 1)

tenth_dimension_values = apply_fractal_function(vertices[:, 0], vertices[:, 1], vertices[:, 2], recursion_depth)

# Plot projected vertices with labels
labels = [''.join(str(v) for v in vertex) for vertex in vertices]
sc = ax.scatter(projected_vertices[:, 0], projected_vertices[:, 1], projected_vertices[:, 2],
                s=100, c=tenth_dimension_values, cmap='viridis', alpha=0.8)
for i, label in enumerate(labels):
    ax.text(projected_vertices[i, 0], projected_vertices[i, 1], projected_vertices[i, 2],
            label, fontsize=8, ha='center', va='center')

# Create illusion lines connecting projected vertices in 3D space
for i in range(len(projected_vertices)):
    for j in range(i + 1, len(projected_vertices)):
        ax.plot([projected_vertices[i, 0], projected_vertices[j, 0]],
                [projected_vertices[i, 1], projected_vertices[j, 1]],
                [projected_vertices[i, 2], projected_vertices[j, 2]], 'k--', alpha=0.3)

# Add a color bar for the tenth dimension
cbar = fig.colorbar(sc, ax=ax, shrink=0.8)
cbar.set_label('Tenth Dimension')

# Display the plot
plt.show()
