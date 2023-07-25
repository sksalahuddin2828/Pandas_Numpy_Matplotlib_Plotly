import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import networkx as nx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import permutations

def is_hamiltonian_cycle(graph):
    n = len(graph)
    vertices = list(range(n))
    for perm in permutations(vertices):
        if graph[perm[-1]][perm[0]] == 1:  # Check if the last vertex is connected to the first vertex
            if all(graph[perm[i]][perm[i+1]] == 1 for i in range(n-1)):  # Check if other vertices are connected in the permutation
                return True
    return False

# Example graph represented as an adjacency matrix
graph_matrix = np.array([[0, 1, 1, 0],
                         [1, 0, 1, 1],
                         [1, 1, 0, 1],
                         [0, 1, 1, 0]])

# Create a NetworkX graph from the adjacency matrix
G = nx.Graph(graph_matrix)

# Create 3D coordinates for nodes using a layout algorithm
pos_3d = nx.spring_layout(G, dim=3, seed=42)

# Define custom colors for nodes and edges
node_color = 'rgb(255, 140, 0)'
edge_color = 'rgb(0, 191, 255)'

# Create a 3D subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])

# Add edges to the subplot
edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = pos_3d[edge[0]]
    x1, y1, z1 = pos_3d[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_z.extend([z0, z1, None])

fig.add_trace(go.Scatter3d(x=edge_x, y=edge_y, z=edge_z, mode='lines', line=dict(color=edge_color, width=3)))

# Add nodes to the subplot
node_x, node_y, node_z = zip(*list(pos_3d.values()))
fig.add_trace(go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='markers', marker=dict(size=10, color=node_color)))

# Add labels to nodes
node_labels = list(G.nodes())
fig.add_trace(go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='text', text=node_labels, textposition='top center',
                           textfont=dict(size=12, color='rgb(0, 0, 0)')))

# Set axis labels and title
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z',
                             xaxis=dict(color='white'),  # Set X-axis label color to white
                             yaxis=dict(color='white'),  # Set Y-axis label color to white
                             zaxis=dict(color='white')),  # Set Z-axis label color to white
                  title='Creative 3D Visualization of Hamiltonian Cycle')

# Add a futuristic background
fig.update_layout(scene=dict(bgcolor='rgb(10, 10, 50)'))

# Animate the Hamiltonian cycle
n = len(G.nodes())
frames = []
for perm in permutations(list(G.nodes())):
    if graph_matrix[perm[-1]][perm[0]] == 1 and all(graph_matrix[perm[i]][perm[i+1]] == 1 for i in range(n-1)):
        frame_data = {
            'data': [
                go.Scatter3d(x=[pos_3d[node][0] for node in perm],
                             y=[pos_3d[node][1] for node in perm],
                             z=[pos_3d[node][2] for node in perm],
                             mode='markers+lines',
                             marker=dict(size=12, color='rgb(255, 255, 0)'),
                             line=dict(color='rgb(255, 165, 0)', width=4))
            ],
            'name': f'Frame {len(frames)}'
        }
        frames.append(frame_data)

# Add animation to the subplot
fig.update(frames=frames)
animation_settings = dict(frame=dict(duration=1000, redraw=True), fromcurrent=True)
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, animation_settings])])])

# Set the layout size to fit within the specified screen width and height
fig.update_layout(width=1280, height=800)

fig.show()
