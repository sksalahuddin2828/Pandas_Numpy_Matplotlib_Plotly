import numpy as np

I = 800.0  # moment of inertia in kg-m^2
initial_angular_velocity = 4.0 * 2 * np.pi  # initial angular velocity in rad/s
final_kinetic_energy = 2.03e5  # final kinetic energy in J

# Calculate new angular velocity
final_angular_velocity = np.sqrt(final_kinetic_energy * 2 / I)

print("Initial Angular Velocity:", initial_angular_velocity, "rad/s")
print("Final Angular Velocity:", final_angular_velocity, "rad/s")


# Answer: Initial Angular Velocity: 25.132741228718345 rad/s
#         Final Angular Velocity: 22.52776065213762 rad/s
