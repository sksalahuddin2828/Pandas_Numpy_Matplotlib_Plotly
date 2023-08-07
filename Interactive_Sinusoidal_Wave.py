from bokeh.plotting import figure, show, output_notebook
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from ipywidgets import interact
import numpy as np
from IPython.display import display

output_notebook()

def sinusoidal_wave(x, A, k, w, phi):
    return A * np.sin(k * x - w * 0 + phi)

x_values = np.linspace(0, 10, 400)
A = 0.5  # Amplitude
k = 2 * np.pi / 5  # Wave number
w = 2 * np.pi / 2  # Angular frequency
phi = np.pi / 4  # Initial phase

p = figure(title='Interactive Sinusoidal Wave', x_axis_label='x', y_axis_label='y',
           width=800, height=400)

source = ColumnDataSource(data={'x': x_values, 'y': sinusoidal_wave(x_values, A, k, w, phi)})
p.line('x', 'y', source=source, line_width=2)

def update_wave(A, k, w, phi):
    new_y = sinusoidal_wave(x_values, A, k, w, phi)
    source.data = {'x': x_values, 'y': new_y}

interact(update_wave, A=(0.1, 1.0, 0.1), k=(0.1, 5.0, 0.1), w=(0.1, 5.0, 0.1), phi=(0, np.pi, 0.1))

display(p)
