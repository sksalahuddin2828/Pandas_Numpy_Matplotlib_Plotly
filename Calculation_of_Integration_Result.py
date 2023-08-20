import numpy as np
import sympy as sp
import plotly.graph_objects as go
import ipywidgets as widgets
import pandas as pd
from IPython.display import display

# Define symbolic variables
x, a = sp.symbols('x a')

# Define the expression and integrate
expression = x * sp.exp(a * x)
integral_result = (1 / a**2) * (a * x - 1) * sp.exp(a * x)

# Initialize interactive sliders
a_slider = widgets.FloatSlider(value=1.0, min=0.1, max=2.0, step=0.1, description='a')
display(a_slider)

# Define x values for plotting
x_values = np.linspace(0, 2, 400)

# Create a figure with Plotly for interactive visualization
fig = go.Figure()

# Create a pandas DataFrame for data management
data = pd.DataFrame(columns=['x', 'Original Function', 'Integrated Result'])

# Define update function for slider
def update_figure(change):
    a_val = a_slider.value
    integrated_y = (np.exp(a_val * x_values) / (a_val**2)) * (a_val * x_values - 1)
    
    fig.data = []  # Clear previous traces
    fig.add_trace(go.Scatter(x=x_values, y=x_values * np.exp(a_val * x_values), name='Original Function'))
    fig.add_trace(go.Scatter(x=x_values, y=integrated_y, name='Integrated Result'))
    
    # Populate the DataFrame
    data['x'] = x_values
    data['Original Function'] = x_values * np.exp(a_val * x_values)
    data['Integrated Result'] = integrated_y

    # Display the updated DataFrame
    print(data)

# Connect slider to the update function
a_slider.observe(update_figure, names='value')

# Update layout for Plotly figure
fig.update_layout(title='Integration of x * e^(a * x)', xaxis_title='x', yaxis_title='y')

# Show the Plotly figure
fig.show()
