import numpy as np
import pandas as pd
import plotly.graph_objects as go

A = 1.0
k = 2.0
ω = 3.0
ϕ = np.pi / 4.0

x = np.linspace(0, 10, 100)
t = np.linspace(0, 5, 50)
X, T = np.meshgrid(x, t)

y = A * np.sin(k * X - ω * T + ϕ)
velocity = A * k * np.cos(k * X - ω * T + ϕ)
acceleration = -A * ω**2 * np.sin(k * X - ω * T + ϕ)

# Create 3D subplots for wave, velocity, and acceleration using Plotly
fig = go.Figure(data=[
    go.Surface(x=X, y=T, z=y, colorscale='viridis', name='Wave'),
    go.Surface(x=X, y=T, z=velocity, colorscale='plasma', name='Velocity'),
    go.Surface(x=X, y=T, z=acceleration, colorscale='inferno', name='Acceleration')
])

fig.update_layout(title='Wave Properties in 3D')
fig.show()

A1 = 0.8
A2 = 0.6
y1 = A1 * np.sin(k * X - ω * T + ϕ)
y2 = A2 * np.cos(k * X - ω * T + ϕ)

combined_y = y1 + y2

fig = go.Figure(data=[
    go.Surface(x=X, y=T, z=combined_y, colorscale='cividis', name='Superposition')
])

fig.update_layout(title='Wave Superposition in 3D')
fig.show()

# Create a DataFrame for interactive selection
df = pd.DataFrame(data=y, columns=x, index=t)

fig = go.Figure(data=[
    go.Surface(z=df.values, x=df.columns, y=df.index, colorscale='viridis')
])

fig.update_layout(title='Interactive Wave Visualization')
fig.update_xaxes(title_text='X')
fig.update_yaxes(title_text='Time')

fig.show()
