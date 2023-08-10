import numpy as np
import plotly.graph_objs as go

# Create data points
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

# Create a figure
fig = go.Figure()

# Add surface plot with color map
surface = go.Surface(x=x, y=y, z=z, colorscale='Viridis')

# Add the surface plot to the figure
fig.add_trace(surface)

# Update layout with labels and title
fig.update_layout(
    title='Creative 3D Plot: z = x^2 + y^2',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)

# Animate rotation
frames = []

for i in range(0, 360, 5):
    frame = go.Frame(data=[go.Surface(
        x=x,
        y=y,
        z=z,
        colorscale='Viridis',
        surfacecolor=z,  # You can adjust this for animation effect
        cmin=z.min(),
        cmax=z.max()
    )])
    camera = dict(eye=dict(x=np.cos(np.radians(i)), y=np.sin(np.radians(i)), z=0.5))
    frame.update(layout=dict(scene_camera=camera))
    frames.append(frame)

# Add frames to the figure
fig.frames = frames

# Set initial frame
fig.data[0].surfacecolor = z

# Configure animation settings
animation_settings = dict(
    frame=dict(duration=50, redraw=True),  # Increase duration for smoother animation
    fromcurrent=True                       # By increasing the duration value (for example, from 50 to 100)
)

# Add animation buttons
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[
    dict(label='Play',
         method='animate',
         args=[None, animation_settings]),
    dict(label='Pause',
         method='animate',
         args=[[None], animation_settings])
])])

# Show the animated plot
fig.show()
