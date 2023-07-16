import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

def rotate_points(points, axis1, axis2, theta):
    # Rotation matrix
    c, s = np.cos(theta), np.sin(theta)
    if axis1 == axis2:
        R = np.array([[c, -s, 0, 0],
                      [s, c, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
    else:
        R = np.array([[c, 0, -s, 0],
                      [0, 1, 0, 0],
                      [s, 0, c, 0],
                      [0, 0, 0, 1]])
    rotated_points = np.dot(points, R)
    return rotated_points

def tesseract_projection():
    # Define the vertices of a tesseract (8 points)
    vertices = np.array([[1, 1, 1, 1],
                         [-1, 1, 1, 1],
                         [-1, -1, 1, 1],
                         [1, -1, 1, 1],
                         [1, 1, -1, 1],
                         [-1, 1, -1, 1],
                         [-1, -1, -1, 1],
                         [1, -1, -1, 1]])

    # Define the edges of the tesseract (connecting vertices)
    edges = [[0, 1], [1, 2], [2, 3], [3, 0],
             [0, 4], [1, 5], [2, 6], [3, 7],
             [4, 5], [5, 6], [6, 7], [7, 4],
             [0, 5], [1, 4], [2, 7], [3, 6]]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set axis limits
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Initialize the animation
    num_frames = 100
    thetas = np.linspace(0, 2 * np.pi, num_frames)

    # Initialize the Poly3DCollection
    poly = [[vertices[edge_idx, :3] for edge_idx in edge] for edge in edges]
    polys = Poly3DCollection(poly, alpha=0.2, facecolors='cyan', linewidths=1, edgecolors='blue')
    ax.add_collection3d(polys)

    def update(frame):
        theta = thetas[frame]
        # Rotate the tesseract
        rotated_vertices = rotate_points(vertices, 1, 2, theta)
        rotated_vertices = rotate_points(rotated_vertices, 0, 3, theta * 0.5)
        # Update the vertices of the Poly3DCollection
        for i, edge in enumerate(edges):
            for j, edge_idx in enumerate(edge):
                polys._vec[j].set_facecolor('cyan')
                polys._vec[j].set_edgecolor('blue')
                polys._verts3d[i][j] = rotated_vertices[edge_idx, :3]
        
    # Create the animation
    ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)
    plt.show()

if __name__ == "__main__":
    tesseract_projection()
