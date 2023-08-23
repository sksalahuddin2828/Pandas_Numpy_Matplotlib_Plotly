import numpy as np
import plotly.express as px

# Generate random data
np.random.seed(42)
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

# Create an interactive 3D scatter plot
fig = px.scatter_3d(x=x, y=y, z=z, title='Interactive 3D Scatter Plot')
fig.show()
