import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
import torch
from sklearn.linear_model import LinearRegression

# Calculate initial and final rotational kinetic energies
I = 800.0  # Moment of inertia in kg-m^2
omega_initial = 4.0 * 2 * np.pi  # Initial angular velocity in rad/s
K0 = 0.5 * I * omega_initial**2
Kf = 2.03e5  # New rotational kinetic energy in J
omega_new = np.sqrt(2 * Kf / I)

# Create 3D visualization using Matplotlib
x = [1, 2, 3, 4]  # Replace with actual x data
y = [5, 6, 7, 8]  # Replace with actual y data
z = [10, 8, 6, 4] # Replace with actual z data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

# Solve symbolic equation using Sympy
x = sp.Symbol('x')
equation = sp.Eq(3*x + 2, 8)
solution = sp.solve(equation, x)

# PyTorch example
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float32)
y_train = torch.tensor([2.0, 4.0, 6.0, 8.0], dtype=torch.float32)
model = torch.nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = torch.nn.MSELoss()
for epoch in range(100):
    y_pred = model(x_train)
    loss = loss_fn(y_pred.squeeze(), y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Scikit-learn example
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
sklearn_model = LinearRegression()
sklearn_model.fit(X, y)

# Creating a scatter plot with Plotly
data = {'x': [1, 2, 3, 4], 'y': [2, 4, 6, 8]}
df = pd.DataFrame(data)
scatter_fig = px.scatter(df, x='x', y='y', title='Scatter Plot')

# Creating a 2D plot with Plotly
x_vals = np.linspace(0, 10, 100)
y_vals = np.sin(x_vals)
sine_fig = px.line(x=x_vals, y=y_vals, title='Sine Curve')
sine_fig.update_xaxes(title='X-axis')
sine_fig.update_yaxes(title='Y-axis')

# Show the Plotly visualizations
scatter_fig.show()
sine_fig.show()
