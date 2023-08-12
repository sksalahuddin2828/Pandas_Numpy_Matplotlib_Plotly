import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create unit vectors
unit_vectors = np.array([[1, 0], [0, 1]])

# Create figure
fig = make_subplots(rows=1, cols=2, subplot_titles=["Original Vectors", "Transformed Vectors"],
                    shared_xaxes=True, shared_yaxes=True)

# Add original unit vectors to the plot
original_vectors_trace = go.Scatter(x=unit_vectors[0], y=unit_vectors[1], mode='markers', name='Original Vectors')
fig.add_trace(original_vectors_trace, row=1, col=1)

# Set axis properties
axis_properties = dict(showgrid=False, zeroline=False, showticklabels=False,
                       range=[-1.5, 1.5], scaleanchor="x", scaleratio=1)
fig.update_xaxes(axis_properties, row=1, col=1)
fig.update_yaxes(axis_properties, row=1, col=1)

# Create an orthogonal matrix
theta = np.radians(30)
orthogonal_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Create a list to store frames
frames = []

# Calculate transformed vectors for each step
num_frames = 50
for i in range(num_frames):
    step_matrix = np.linalg.matrix_power(orthogonal_matrix, int(i * 2 / num_frames))
    transformed_vectors = np.dot(step_matrix, unit_vectors)
    
    # Create a scatter plot for transformed vectors in each step
    transformed_vectors_trace = go.Scatter(x=transformed_vectors[0], y=transformed_vectors[1],
                                           mode='markers', name='Transformed Vectors')
    frame = go.Frame(data=[transformed_vectors_trace])
    frames.append(frame)

# Add frames to the animation
fig.frames = frames

# Define animation settings
animation_settings = dict(frame=dict(duration=100, redraw=True),
                          fromcurrent=True,
                          transition=dict(duration=300, easing="quadratic-in-out"))

# Add play and pause buttons to the animation
fig.update_layout(updatemenus=[
    dict(type="buttons", showactive=False, buttons=[
        dict(label="Play", method="animate", args=[None, animation_settings]),
        dict(label="Pause", method="animate", args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate")])
    ])
])

# Set layout and show the animation
fig.update_layout(title="Orthogonal Matrix Transformation Animation",
                  showlegend=False, width=1000, height=500)

# Add animation frames to the layout
fig.frames = frames

# Show the animation
fig.show()
