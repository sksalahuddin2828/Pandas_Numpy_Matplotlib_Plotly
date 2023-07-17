import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate random 7D data with specific patterns
np.random.seed(42)
num_samples = 100
data_7d = np.random.rand(num_samples, 7)

# Map the 7D data patterns to colors
data_colors = data_7d[:, 3:6]  # Use dimensions 4, 5, and 6 for RGB values

# Map the 7D data patterns to sizes
data_sizes = np.sum(data_7d[:, 0:3], axis=1)  # Use dimensions 1, 2, and 3 for sizes

# Create the interactive 3D plot with larger figure size
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]], print_grid=False)
fig.update_layout(width=800, height=800)  # Adjust the figure size here

# Add data points to the 3D plot
fig.add_trace(
    go.Scatter3d(
        x=data_7d[:, 0],
        y=data_7d[:, 1],
        z=data_7d[:, 2],
        mode='markers',
        marker=dict(
            size=data_sizes * 10,
            color=data_colors,
            colorscale='Viridis',
            opacity=0.8
        )
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
