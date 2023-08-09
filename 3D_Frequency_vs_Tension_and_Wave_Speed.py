import numpy as np
import pandas as pd
import plotly.graph_objs as go
from sympy import symbols, sqrt, Eq, solve

# Constants
mu = 0.03
length = 2.0

# Symbols for tension, wave speed, and frequency
tension, wave_speed, frequency = symbols('tension wave_speed frequency')

# Equations
wave_speed_eq = Eq(wave_speed, sqrt(tension / mu))
frequency_eq = Eq(frequency, wave_speed / length)

# Generate tension values
tension_values = np.linspace(10, 40, 100)

# Calculate wave speeds and frequencies
wave_speeds = [float(solve(wave_speed_eq.subs(tension, t))[0]) for t in tension_values]
frequencies = [float(solve(frequency_eq.subs(wave_speed, ws))[0]) for ws in wave_speeds]

# Create a DataFrame
results_df = pd.DataFrame({'Tension (N)': tension_values, 'Wave Speed (m/s)': wave_speeds, 'Frequency (Hz)': frequencies})

# 3D Scatter plot
fig = go.Figure(data=[go.Scatter3d(x=tension_values, y=wave_speeds, z=frequencies, mode='markers', marker=dict(size=5))])
fig.update_layout(scene=dict(xaxis_title='Tension (N)', yaxis_title='Wave Speed (m/s)', zaxis_title='Frequency (Hz)'),
                  title='Frequency vs. Tension and Wave Speed', margin=dict(l=0, r=0, b=0, t=40))

# Animation frames
animation_frames = []
for i in range(len(tension_values)):
    frame = go.Frame(data=[go.Scatter3d(x=tension_values[:i+1], y=wave_speeds[:i+1], z=frequencies[:i+1], mode='markers',
                                         marker=dict(size=5))])
    animation_frames.append(frame)

fig.frames = animation_frames

# Slider for animation
sliders = [dict(steps=[dict(args=[['frame', f.name], {'frame': {'duration': 100, 'redraw': True}, 'mode': 'immediate'}],
                            label=str(i))
                 for i, f in enumerate(fig.frames)],
                active=0)]

fig.update_layout(sliders=sliders)

# Show the interactive 3D visualization
fig.show()
