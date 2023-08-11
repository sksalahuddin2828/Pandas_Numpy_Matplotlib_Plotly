import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Define the non-linear equation
def nonlinear_equation(x):
    return x**2 + np.sin(x)

# Generate x values
x = np.linspace(-5, 100, 400)

# Calculate corresponding y values using the equation
y = nonlinear_equation(x)

# Create a DataFrame for the data
data = pd.DataFrame({'x': x, 'y': y})

# Create animated plot using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Create scatter trace
scatter_trace = go.Scatter(x=data['x'], y=data['y'], mode='markers')
fig.add_trace(scatter_trace)

# Create line trace
line_trace = go.Scatter(x=[], y=[], mode='lines', line=dict(color='red'))
fig.add_trace(line_trace)

# Create animation frames
frames = [go.Frame(data=[go.Scatter(x=data['x'][:i], y=data['y'][:i], mode='markers'),
                         go.Scatter(x=[data['x'][i]], y=[data['y'][i]], mode='markers', marker=dict(size=10, color='red'))],
                   traces=[0, 1]) for i in range(2, len(data))]

# Update animation frames
fig.frames = frames

# Update layout for animation
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                  buttons=[dict(label='Play',
                                                method='animate',
                                                args=[None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True,
                                                             'transition': {'duration': 0}}]),
                                           dict(label='Pause',
                                                method='animate',
                                                args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'after',
                                                             'transition': {'duration': 0}}])])])

fig.update_layout(title='Animated Non-linear Equation Visualization',
                  xaxis_title='x',
                  yaxis_title='y')

# Show the plot
fig.show()
