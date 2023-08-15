# pip install dash

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Create a Dash app
app = dash.Dash(__name__)

# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Initial parameters
num_terms = 5
freq_sliders = [dcc.Slider(id=f'freq-slider-{i}', min=1, max=20, step=1, value=1) for i in range(num_terms)]

# Layout of the app
app.layout = html.Div([
    dcc.Graph(figure=fig),
    html.Div(freq_sliders, id='freq-slider-container')
])

# Update the figure based on slider values
@app.callback(
    Output('freq-slider-container', 'children'),
    Output('figure', 'figure'),
    Input('freq-slider-0', 'value'),
    Input('freq-slider-1', 'value'),
    Input('freq-slider-2', 'value'),
    Input('freq-slider-3', 'value'),
    Input('freq-slider-4', 'value')
)
def update_figure(freq_0, freq_1, freq_2, freq_3, freq_4):
    t_vals = np.linspace(0, 2 * np.pi, 1000)
    x = np.zeros_like(t_vals)
    y = np.zeros_like(t_vals)
    
    for i, freq in enumerate([freq_0, freq_1, freq_2, freq_3, freq_4]):
        x += np.cos((i + 1) * t_vals * freq)
        y += np.sin((i + 1) * t_vals * freq)
    
    x /= num_terms
    y /= num_terms
    
    # Create scatter plot
    scatter_trace = go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue'))
    
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])
    fig.add_trace(scatter_trace)
    fig.update_layout(
        title='Creative Fourier Series Visualization',
        xaxis_title='X',
        yaxis_title='Y',
    )
    
    return freq_sliders, fig

if __name__ == '__main__':
    app.run_server(debug=True)
