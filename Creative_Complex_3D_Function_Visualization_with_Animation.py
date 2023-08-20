import numpy as np
import plotly.express as px
import pandas as pd

# Define the function to be visualized
def complex_function(x_val, a_val):
    return np.exp(-a_val) * np.sin(x_val) * np.sqrt(a_val**2 + x_val**2)

# Create x and a values
x_vals = np.linspace(0, 5, 100)
a_vals = np.linspace(0.1, 5, 50)

# Create meshgrid
X, A = np.meshgrid(x_vals, a_vals)
Z = complex_function(X, A)

# Create a DataFrame
df = pd.DataFrame({'x': X.flatten(), 'a': A.flatten(), 'value': Z.flatten()})

# Create an interactive 3D surface plot with dynamic color transitions and animation
fig = px.scatter_3d(df, x='x', y='a', z='value', opacity=0.7,
                    title='Creative Complex 3D Function Visualization with Animation',
                    labels={'value': 'Function Value'},
                    color='value',
                    color_continuous_scale=px.colors.sequential.Viridis,
                    animation_frame='a')  # Animation frame parameter

# Update animation settings for smoother rotation
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                method='animate', args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True, mode='immediate')])])])

# Add rotating animation effect by setting frame animation duration
rotation_frames = []
for angle in np.linspace(0, 360, len(a_vals)):
    rotation_frames.append(go.Frame(layout_scene=dict(camera_eye=dict(x=0, y=1, z=0),  # Adjust the camera eye position for rotation
                                                     xaxis_title='x', yaxis_title='a', zaxis_title='Function Value')))
fig.frames = rotation_frames

# Add slider for animation speed control
fig.update_layout(sliders=[dict(currentvalue=dict(prefix='Speed: ', visible=True),
                                steps=[dict(label=str(duration), method='animate', args=[[None], dict(frame=dict(duration=duration, redraw=True), mode='immediate')]) for duration in [100, 50, 10, 1]])])

fig.show()
