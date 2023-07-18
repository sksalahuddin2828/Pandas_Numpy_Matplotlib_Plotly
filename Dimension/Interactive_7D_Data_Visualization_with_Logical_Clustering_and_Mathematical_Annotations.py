# Interactive 7D Data Visualization with Logical Clustering and Mathematical Annotations.

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans

# Generate random 7D data with specific patterns
np.random.seed(42)
num_samples = 100
data_7d = np.random.rand(num_samples, 7)

# Perform clustering on the data
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data_labels = kmeans.fit_predict(data_7d)

# Map the 7D data patterns to colors
data_colors = data_labels

# Map the 7D data patterns to sizes
data_sizes = np.sum(data_7d[:, 0:3], axis=1)  # Use dimensions 1, 2, and 3 for sizes

# Create the interactive 3D plot with larger figure size
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]], print_grid=False)
fig.update_layout(width=800, height=800)  # Adjust the figure size here

# Add data points to the 3D plot
for i in range(num_samples):
    fig.add_trace(
        go.Scatter3d(
            x=[data_7d[i, 0]],
            y=[data_7d[i, 1]],
            z=[data_7d[i, 2]],
            mode='markers',
            marker=dict(
                size=data_sizes[i] * 20,
                color=data_colors[i],
                colorscale='Viridis',
                opacity=0.8
            ),
            text=f'Cluster: {data_labels[i]}<br>Data point: {i}',
            hoverinfo='text'
        )
    )

# Set plot layout and axis labels
fig.update_layout(
    scene=dict(
        xaxis_title='Dimension 1',
        yaxis_title='Dimension 2',
        zaxis_title='Dimension 3',
        xaxis=dict(range=[0, 1]),
        yaxis=dict(range=[0, 1]),
        zaxis=dict(range=[0, 1])
    )
)

# Show the interactive plot
fig.show()
