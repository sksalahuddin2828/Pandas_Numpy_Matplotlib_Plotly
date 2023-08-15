import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ipywidgets import interact, widgets
from IPython.display import display

# Create a pandas DataFrame to store data
num_points = 1000
t_vals = np.linspace(0, 2 * np.pi, num_points)
df = pd.DataFrame({'t': t_vals})

# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Initial parameters
num_terms = 5
freq_sliders = [widgets.IntSlider(value=1, min=1, max=20, step=1, description=f'Freq {i+1}') for i in range(num_terms)]
slider_container = widgets.HBox(freq_sliders)

# Update function for sliders
def update_sliders(change):
    update_figure()

for slider in freq_sliders:
    slider.observe(update_sliders, names='value')

# Update the figure based on slider values
def update_figure():
    x = np.zeros(num_points)
    y = np.zeros(num_points)

    for i, slider in enumerate(freq_sliders):
        freq = slider.value
        x += np.cos((i + 1) * t_vals * freq)
        y += np.sin((i + 1) * t_vals * freq)

    x /= num_terms
    y /= num_terms
    
    # Update scatter plot
    fig.update_traces(x=x, y=y)
    fig.update_layout(
        title='Creative Fourier Series Visualization',
        xaxis_title='X',
        yaxis_title='Y',
    )

update_figure()

# Display interactive visualization
display(slider_container)
fig.show()
