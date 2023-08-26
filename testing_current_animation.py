import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Constants
R = 100  # Resistance in ohms
L = 0.1  # Inductance in H
C = 0.01  # Capacitance in F

def update_plot(freq):
    omega = 2 * np.pi * freq
    impedance = np.sqrt(R**2 + (omega*L - 1/(omega*C))**2)
    phase_angle = np.arctan((omega*L - 1/(omega*C)) / R)
    
    plt.figure(figsize=(10, 6))
    plt.plot(freq, impedance, 'bo', label='Impedance')
    plt.plot(freq, phase_angle, 'ro', label='Phase Angle')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Value')
    plt.title('Impedance and Phase Angle vs Frequency')
    plt.legend()
    plt.grid()
    plt.show()

freq_slider = widgets.FloatSlider(value=50, min=1, max=1000, step=1, description='Frequency (Hz)')
widgets.interactive(update_plot, freq=freq_slider)

def plot_frequency_domain(freq, num_harmonics):
    t = np.linspace(0, 1, 1000)
    signal = np.sin(2 * np.pi * freq * t)  # Fundamental frequency
    
    for n in range(2, num_harmonics + 1):
        harmonic = np.sin(2 * np.pi * n * freq * t) / n
        signal += harmonic
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(f'Composite Signal (Fundamental Frequency = {freq} Hz)')
    plt.grid()
    plt.show()

freq_slider = widgets.FloatSlider(value=50, min=1, max=1000, step=1, description='Frequency (Hz)')
num_harmonics_slider = widgets.IntSlider(value=5, min=1, max=20, step=1, description='Num Harmonics')
widgets.interactive(plot_frequency_domain, freq=freq_slider, num_harmonics=num_harmonics_slider)

def plot_lissajous(freq_ratio, phase_difference):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(freq_ratio * t)
    y = np.sin(t + phase_difference)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title(f'Lissajous Figure (Frequency Ratio: {freq_ratio}, Phase Difference: {phase_difference:.2f})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.show()

freq_ratio_slider = widgets.FloatSlider(value=2, min=0.1, max=10, step=0.1, description='Freq Ratio')
phase_difference_slider = widgets.FloatSlider(value=0, min=0, max=2*np.pi, step=0.1, description='Phase Difference')
widgets.interactive(plot_lissajous, freq_ratio=freq_ratio_slider, phase_difference=phase_difference_slider)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

fig, ax = plt.subplots()
x_vals = np.linspace(0, 2 * np.pi, 100)
equations = [
    ('$y = \sin(x)$', np.sin(x_vals)),
    ('$y = \cos(x)$', np.cos(x_vals)),
    ('$y = \sin(x) + \cos(x)$', np.sin(x_vals) + np.cos(x_vals))
]
line, = ax.plot(x_vals, equations[0][1], lw=2)

def animate(i):
    line.set_ydata(equations[i][1])
    ax.set_title(equations[i][0])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(equations), interval=2000, blit=True)
HTML(ani.to_jshtml())
