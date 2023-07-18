import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_hypercube_edges(dimensions):
    num_vertices = 2 ** dimensions
    gray_codes = np.arange(num_vertices) ^ np.arange(num_vertices) >> 1
    edges = []
    for i in range(num_vertices):
        for j in range(dimensions):
            neighbor = i ^ (1 << j)
            if gray_codes[i] < gray_codes[neighbor]:
                edges.append((i, neighbor))
    return edges

# Define the number of dimensions for the hypercube
num_dimensions = 5

# Generate hypercube edges
edges = generate_hypercube_edges(num_dimensions)

# Create a figure and axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.axis('off')

# Plot the hypercube edges with modified transparency and linewidth
for edge in edges:
    vertices = np.array([
        [-1 if (vertex >> i) & 1 else 1 for i in range(num_dimensions)]
        for vertex in edge
    ])
    ax.plot3D(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='red', alpha=0.2, linewidth=1.0)

# Define rotation matrices for different dimensions
angles = np.linspace(0, 2 * np.pi, num_dimensions + 1)[:-1]
rotation_matrices = [
    np.array([[np.cos(angle), -np.sin(angle), 0],
              [np.sin(angle), np.cos(angle), 0],
              [0, 0, 1]])
    for angle in angles
]

# Generate hypercube vertices
num_vertices = 2 ** num_dimensions
vertices = np.array([
    [-1 if (vertex >> i) & 1 else 1 for i in range(num_dimensions)]
    for vertex in range(num_vertices)
])

# Apply rotations to the vertices
projected_vertices = vertices[:, :3]
for i in range(3, num_dimensions):
    projected_vertices = np.dot(projected_vertices, rotation_matrices[i])

# Add random offsets to each vertex
offsets = np.random.uniform(low=-0.2, high=0.2, size=(num_vertices, 3))
projected_vertices += offsets

# Plot projected vertices with labels
labels = [''.join(str(v) for v in vertex) for vertex in vertices]
sc = ax.scatter(projected_vertices[:, 0], projected_vertices[:, 1], projected_vertices[:, 2],
                s=100, c=projected_vertices[:, 2], cmap='viridis', alpha=0.8)
for i, label in enumerate(labels):
    ax.text(projected_vertices[i, 0], projected_vertices[i, 1], projected_vertices[i, 2],
            label, fontsize=8, ha='center', va='center')

# Create illusion lines connecting projected vertices in 3D space
for i in range(len(projected_vertices)):
    for j in range(i + 1, len(projected_vertices)):
        ax.plot([projected_vertices[i, 0], projected_vertices[j, 0]],
                [projected_vertices[i, 1], projected_vertices[j, 1]],
                [projected_vertices[i, 2], projected_vertices[j, 2]], 'k--', alpha=0.1)

# Add a color bar for the third dimension
cbar = fig.colorbar(sc, ax=ax, shrink=0.8)
cbar.set_label('Third Dimension')

# Display the plot
plt.show()
