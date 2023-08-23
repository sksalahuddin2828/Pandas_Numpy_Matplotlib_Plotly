import numpy as np
import sympy as sp

# Given data
alpha = 20.0 * (2 * np.pi) - 0.1 * sp.Symbol('t')  # rad/s^2
t = 10.0  # s

# Calculating angular velocity and displacement
angular_velocity = sp.integrate(alpha, ('t', 0, t))
displacement = sp.integrate(angular_velocity, ('t', 0, t))

# Convert angular_velocity and displacement to numeric values
angular_velocity_numeric = angular_velocity.subs('t', t)
displacement_numeric = displacement.subs('t', t)

print("Angular Velocity:", angular_velocity_numeric)
print("Displacement:", displacement_numeric)


# Answer: Angular Velocity: 1251.63706143592
#         Displacement: 12516.3706143592
