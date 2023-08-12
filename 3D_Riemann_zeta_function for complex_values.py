import numpy as np
import plotly.express as px
from sympy import zeta
from sympy.abc import s

# Define the Riemann zeta function using SymPy
def riemann_zeta(s):
    return zeta(s)

# Generate complex values along the critical line
s_real = np.linspace(0.1, 20, 100)
s_complex = s_real + 1j

# Evaluate the Riemann zeta function for complex values using SymPy
zeta_values = np.array([riemann_zeta(complex(r, i)).evalf() for r, i in zip(np.real(s_complex), np.imag(s_complex))])

# Create a Plotly figure for interactive visualization
fig = px.scatter(x=np.real(s_complex), y=np.imag(zeta_values), title='Approximated Riemann Zeta Function',
                 labels={'x': 'Real Part', 'y': 'Imaginary Part'})

# Customize the appearance of the scatter plot
fig.update_traces(mode='lines+markers', marker=dict(size=5, color='blue'))

# Show the Plotly figure
fig.show()
