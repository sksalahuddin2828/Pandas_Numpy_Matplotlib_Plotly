import matplotlib.pyplot as plt
import numpy as np
import sys 
import time

def circle_dance(population=11, resolution=480, loops=1, flip=0, lines=0):
    population = int(population)
    resolution = int(resolution)
    radius = 250
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    if lines:
        arrange_lines(ax, population, radius)
    dancers = []
    for i in range(population):
        dancer = make_dancer(i, population)
        dancers.append(dancer)
    animate(dancers, resolution, fig, ax, loops, flip, radius)


def arrange_lines(ax, population, radius):
    for n in range(population):
        angle = n / population * np.pi
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        ax.plot([-x, x], [-y, y], color='black')


def make_dancer(i, population):
    angle = i / population * np.pi
    color = random_turtle_colour()
    return (angle, color)


def random_turtle_colour():
    return [np.random.uniform(0, 0.9), 0.5 + np.random.uniform(0, 0.5), np.random.uniform(0, 0.7)]


def animate(dancers, resolution, fig, ax, loops, flip, radius):
    delay = 4 / resolution      # 4 seconds per repetition
    phases = np.linspace(0, 2 * np.pi, resolution)
    while True:
        for i, phase in enumerate(phases):
            timer = time.perf_counter()
            draw_dancers(dancers, phase, ax, loops, flip, radius)
            plt.pause(0.001)
            fig.canvas.draw_idle()
            elapsed = time.perf_counter() - timer
            adjusted_delay = max(0, delay - elapsed)
            time.sleep(adjusted_delay)


def draw_dancers(dancers, phase, ax, loops, flip, radius):
    population = len(dancers)
    for i in range(population):
        individual_phase = (phase + dancers[i][0] * loops * np.pi) % (2 * np.pi)
        angle = individual_phase
        if flip:
            if np.pi / 2 < angle <= 3 * np.pi / 2:
                tilt_angle = np.pi
            else:
                tilt_angle = 0
        else:
            tilt_angle = 0
        distance = radius * np.sin(angle)
        x = distance * np.cos(dancers[i][0])
        y = distance * np.sin(dancers[i][0])
        color = dancers[i][1]
        ax.plot(x, y, 'o', color=color)
        ax.set_xlim(-radius, radius)
        ax.set_ylim(-radius, radius)
        ax.axis('off')


if __name__ == '__main__':
    circle_dance(*(float(n) for n in sys.argv[1:]))
