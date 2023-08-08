import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Constants
A = 1.0
k = 2.0
ω = 3.0
ϕ = np.pi / 4.0

# Generate data
x = np.linspace(0, 10, 100)  # Spatial coordinates
t = np.linspace(0, 5, 50)    # Time coordinates

X, T = np.meshgrid(x, t)     # Meshgrid for 3D plot

# Compute wave function
y = A * np.sin(k * X - ω * T + ϕ)

# Create a 3D plot using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])
fig.add_trace(go.Surface(x=X, y=T, z=y, colorscale='viridis'))

# Update layout for 3D visualization
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Time', zaxis_title='Amplitude'),
                  scene_camera=dict(eye=dict(x=1.5, y=1.5, z=0.7)))

fig.update_layout(title='Wave Propagation in 3D')

fig.show()
