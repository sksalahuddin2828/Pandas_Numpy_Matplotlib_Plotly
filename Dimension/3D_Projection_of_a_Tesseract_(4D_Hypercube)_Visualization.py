import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def tesseract_projection():
    # Define the vertices of a unit tesseract in 4D space
    vertices = np.array([
        [-0.5, -0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5, -0.5],
        [-0.5, 0.5, -0.5, -0.5],
        [-0.5, -0.5, 0.5, -0.5],
        [0.5, -0.5, 0.5, -0.5],
        [0.5, 0.5, 0.5, -0.5],
        [-0.5, 0.5, 0.5, -0.5],
        [-0.5, -0.5, -0.5, 0.5],
        [0.5, -0.5, -0.5, 0.5],
        [0.5, 0.5, -0.5, 0.5],
        [-0.5, 0.5, -0.5, 0.5],
        [-0.5, -0.5, 0.5, 0.5],
        [0.5, -0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5, 0.5],
    ])

    # Define the edges of the tesseract
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7],
        [8, 9], [9, 10], [10, 11], [11, 8],
        [12, 13], [13, 14], [14, 15], [15, 12],
        [8, 12], [9, 13], [10, 14], [11, 15],
        [0, 8], [1, 9], [2, 10], [3, 11],
        [4, 12], [5, 13], [6, 14], [7, 15],
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Project the tesseract's vertices to 3D space
    projection_3d = (vertices[:, :-1] + vertices[:, 1:]) / 2.0

    # Plot the edges
    for edge in edges:
        ax.plot3D(*zip(*projection_3d[edge]), color='b')

    # Plot the faces of the tesseract
    faces = Poly3DCollection([projection_3d[[*face]] for face in [
        [0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
        [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5],
        [8, 9, 10, 11], [12, 13, 14, 15], [8, 9, 13, 12],
        [10, 11, 15, 14], [8, 11, 15, 12], [9, 10, 14, 13],
        [0, 8, 12, 4], [1, 9, 13, 5], [2, 10, 14, 6], [3, 11, 15, 7]
    ]], alpha=0.25, facecolors='cyan', edgecolors='r')
    ax.add_collection3d(faces)

    # Set the axis limits and labels
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title('3D Projection of a Tesseract (4D Hypercube)')
    plt.show()

if __name__ == "__main__":
    tesseract_projection()
