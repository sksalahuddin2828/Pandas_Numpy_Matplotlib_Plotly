import numpy as np
import plotly.graph_objects as go

# Number of frames and matrix size
num_frames = 30
matrix_size = 10

# Initialize the first matrix
current_matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size))
current_matrix = (current_matrix + current_matrix.T) / 2  # Ensure symmetry

# Create the figure
fig = go.Figure()

# Create frames for the animation
for _ in range(num_frames):
    # Add some random noise to the current matrix
    random_offset = np.random.uniform(-2, 2, size=(matrix_size, matrix_size))
    new_matrix = current_matrix + random_offset
    new_matrix = (new_matrix + new_matrix.T) / 2  # Ensure symmetry
    fig.add_trace(
        go.Surface(z=new_matrix, colorscale='Viridis')
    )
    current_matrix = new_matrix

# Set layout
fig.update_layout(
    scene=dict(
        xaxis_title="Columns",
        yaxis_title="Rows",
        zaxis_title="Values",
        aspectmode="data",
        camera=dict(eye=dict(x=-1.5, y=-1.5, z=1))
    ),
    title="Creative Animation: Random Walk of Symmetric Matrices",
    width=1200,
    height=800,
    font=dict(size=10)
)

# Display the 3D animation
fig.show()
