import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Create an array of matrices for animation
num_frames = 10
matrices = [np.array([[4 + i, 3 + i], [2 + i, 1 + i]]) for i in range(num_frames)]

# Convert matrices to pandas DataFrames
dfs = [pd.DataFrame(mat, columns=['Column 1', 'Column 2']) for mat in matrices]

# Create animated heatmap using plotly
fig = px.imshow(dfs[0], labels=dict(color="Matrix A"), title="Animated Heatmap of Matrix A")

frames = [go.Frame(data=[go.Heatmap(z=dfs[i].values, colorscale='Viridis')]) for i in range(num_frames)]
fig.frames = frames

fig.update(frames=[go.Frame(data=[go.Heatmap(z=df.values, colorscale='Viridis')]) for df in dfs])
fig.show()
