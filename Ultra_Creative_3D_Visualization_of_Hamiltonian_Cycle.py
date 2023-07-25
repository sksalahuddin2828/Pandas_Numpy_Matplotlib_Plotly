import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import networkx as nx
import plotly.graph_objects as go
from itertools import permutations
import time

def is_hamiltonian_cycle(graph):
    n = len(graph)
    vertices = list(range(n))
    for perm in permutations(vertices):
        if graph[perm[-1]][perm[0]] == 1:  # Check if the last vertex is connected to the first vertex
            if all(graph[perm[i]][perm[i+1]] == 1 for i in range(n-1)):  # Check if other vertices are connected in the permutation
                return True
    return False

# Example graph represented as an adjacency matrix
graph_matrix = np.array([[0, 1, 1, 1, 0, 0, 0, 1],
                         [1, 0, 1, 1, 0, 1, 0, 0],
                         [1, 1, 0, 1, 1, 0, 1, 0],
                         [1, 1, 1, 0, 1, 0, 0, 0],
                         [0, 0, 1, 1, 0, 1, 1, 1],
                         [0, 1, 0, 0, 1, 0, 1, 1],
                         [0, 0, 1, 0, 1, 1, 0, 1],
                         [1, 0, 0, 0, 1, 1, 1, 0]])

# Create a NetworkX graph from the adjacency matrix
G = nx.Graph(graph_matrix)

# Create 3D coordinates for nodes manually
pos_3d = {0: (1, 1, 1), 1: (1, 2, 1), 2: (2, 1, 1), 3: (2, 2, 1),
          4: (1, 1, 2), 5: (1, 2, 2), 6: (2, 1, 2), 7: (2, 2, 2)}

# Create an initial empty 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the graph in 3D with generative art techniques and animation
edge_trace = None
node_colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']

for edge in G.edges():
    x0, y0, z0 = pos_3d[edge[0]]
    x1, y1, z1 = pos_3d[edge[1]]
    line = [(x0, y0, z0), (x1, y1, z1)]
    edge_trace = Line3DCollection([line], color=np.random.choice(node_colors), linewidths=2) if edge_trace is None else \
                 Line3DCollection([line], color=np.random.choice(node_colors), linewidths=2, alpha=0.3)
    ax.add_collection3d(edge_trace)

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Ultra Creative 3D Visualization of Hamiltonian Cycle')

# Add dynamic effects with rotation and scaling
for angle in range(0, 360, 5):
    ax.view_init(30, angle)
    ax.dist = 9 - angle/20  # Add scaling effect
    plt.draw()
    plt.pause(0.01)

# Add artistic elements with a custom background color
ax.w_xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
ax.w_yaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
ax.w_zaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
ax.set_facecolor((0.9, 0.9, 0.9, 1.0))

plt.show()
