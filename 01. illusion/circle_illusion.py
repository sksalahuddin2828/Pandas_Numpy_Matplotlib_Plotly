import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def x(num_points, point_index):
    return 3 * np.cos(np.pi / num_points * point_index)

def y(num_points, point_index):
    return 3 * np.sin(np.pi / num_points * point_index)

def X(num_points, point_index, t):
    return x(num_points, point_index) * np.cos(t + np.pi / num_points * point_index)

def Y(num_points, point_index, t):
    return y(num_points, point_index) * np.cos(t + np.pi / num_points * point_index)

num_points = 10
times = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()

def animate(t):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.plot(3 * np.cos(times), 3 * np.sin(times), 'yo')  # static point

    for i in range(1, num_points + 1):
        ax.plot([-x(num_points, i), x(num_points, i)], [-y(num_points, i), y(num_points, i)], 'y-')  # lines
        ax.plot(X(num_points, i, t), Y(num_points, i, t), 'wo')  # oscillated points

ani = animation.FuncAnimation(fig, animate, frames=len(times), interval=100)
plt.show()
