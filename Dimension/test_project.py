import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# from IPython.display import HTML
# plt.rcParams['animation.html'] = 'jshtml'

# Define tesseract vertices
vertices = np.array([[-1, -1, -1, -1],
                     [-1, -1, -1,  1],
                     [-1, -1,  1, -1],
                     [-1, -1,  1,  1],
                     [-1,  1, -1, -1],
                     [-1,  1, -1,  1],
                     [-1,  1,  1, -1],
                     [-1,  1,  1,  1],
                     [ 1, -1, -1, -1],
                     [ 1, -1, -1,  1],
                     [ 1, -1,  1, -1],
                     [ 1, -1,  1,  1],
                     [ 1,  1, -1, -1],
                     [ 1,  1, -1,  1],
                     [ 1,  1,  1, -1],
                     [ 1,  1,  1,  1]])

# Define edges of the tesseract
edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7),
         (4, 5), (4, 6), (5, 7), (6, 7), (8, 9), (8, 10), (8, 12), (9, 11),
         (9, 13), (10, 11), (10, 14), (11, 15), (12, 13), (12, 14), (13, 15),
         (14, 15), (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14),
         (7, 15)]

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.axis('off')

# Function to update the plot for animation
def update_plot(frame):
    ax.cla()  # Clear previous frame
    ax.set_aspect('auto')
    ax.axis('off')

    # Define rotation matrices for each axis
    angle_x = frame
    angle_y = frame
    angle_z = frame
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, np.cos(angle_x), -np.sin(angle_x)],
                                  [0, np.sin(angle_x), np.cos(angle_x)]])
    rotation_matrix_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                                  [0, 1, 0],
                                  [-np.sin(angle_y), 0, np.cos(angle_y)]])
    rotation_matrix_z = np.array([[np.cos(angle_z), -np.sin(angle_z), 0],
                                  [np.sin(angle_z), np.cos(angle_z), 0],
                                  [0, 0, 1]])

    # Rotate the tesseract
    rotated_vertices = np.dot(vertices, rotation_matrix_x)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_y)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_z)

    # Plot the tesseract faces
    faces = [[rotated_vertices[j] for j in face] for face in edges]
    ax.add_collection3d(Poly3DCollection(faces, linewidths=1, edgecolors='black', alpha=0.4))

    # Set the plot limits to fit the tesseract
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    # Set the view angle
    ax.view_init(elev=20, azim=45 + frame * 180 / np.pi)

# Animate the plot
frames = np.linspace(0, 2 * np.pi, 100)
animation = FuncAnimation(fig, update_plot, frames=frames, interval=50)

# animation = FuncAnimation(fig, update_plot, frames=frames, interval=50)
# HTML(animation.to_jshtml())

# Display the animation
plt.show()
