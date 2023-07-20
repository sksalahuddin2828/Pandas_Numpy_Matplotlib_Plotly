import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display

def bizarrely_universe(num_galaxies, num_dimensions):
    return np.random.randn(num_galaxies, num_dimensions)

def central_limit_theorem(num_galaxies, num_dimensions, num_samples, sample_size):
    sample_means = []
    for _ in range(num_samples):
        galaxies = bizarrely_universe(num_galaxies, num_dimensions)
        mean = np.mean(galaxies[:sample_size])
        sample_means.append(mean)
    return sample_means

def plot_clt(sample_means, num_samples):
    fig, ax = plt.subplots()
    ax.set_xlabel('Sample Means')
    ax.set_ylabel('Probability Density')
    ax.set_title('Central Limit Theorem Visualization')

    # Calculate PDF using Gaussian kernel density estimation
    kde = np.sum([norm(mean, 0.5).pdf(np.linspace(-5, 5, 1000)) for mean in sample_means], axis=0)
    kde /= num_samples

    ax.plot(np.linspace(-5, 5, 1000), kde, color='b', lw=2)

    plt.show()

def animate_clt(num_samples, sample_size, num_galaxies, num_dimensions):
    fig, ax = plt.subplots()
    ax.set_xlabel('Sample Means')
    ax.set_ylabel('Probability Density')
    ax.set_title('Central Limit Theorem Animation')

    # Initialize line plot for probability densities
    line, = ax.plot([], [], color='b', lw=2)

    # Initialize a plot to show the sample means
    sample_means_line, = ax.plot([], [], 'ro', markersize=5)

    def update_hist(num):
        means = central_limit_theorem(num_galaxies, num_dimensions, num_samples, sample_size)
        kde = np.sum([norm(mean, 0.5).pdf(np.linspace(-5, 5, 1000)) for mean in means], axis=0)
        kde /= num_samples

        # Update the line plot for probability densities with the new data
        line.set_data(np.linspace(-5, 5, 1000), kde)

        # Update the plot for sample means
        sample_means_line.set_data(means, np.zeros_like(means))

        # Adjust the y-axis limit to ensure visibility of probability densities
        ax.set_ylim(0, 2)

        # Add annotations for sample means
        for mean in means:
            ax.annotate(f'{mean:.2f}', xy=(mean, 0.05), xytext=(mean, 0.2), arrowprops=dict(arrowstyle='->', color='red'))

        return line, sample_means_line,  # Return both plot objects as a tuple

    ani = FuncAnimation(fig, update_hist, frames=num_samples, interval=500, repeat=True)

    # Display the animation
    plt.show()

# Constants
num_galaxies = 1000
num_dimensions = 3
num_samples = 100
sample_size = 10

# Step 5: Explanation
print("Welcome to the CLT Bizarrely Universe!")
print("In this universe, galaxies are randomly scattered in a 3D space.")
print("Let's visualize the Bizarrely Universe:")

galaxies = bizarrely_universe(num_galaxies, num_dimensions)
plot_bizarrely_universe(galaxies)

print("\nNow, let's apply the Central Limit Theorem.")
print("We'll take {} samples of size {} and observe how their means converge to a Gaussian distribution.".format(num_samples, sample_size))
print("Creating the animation...")

# Display the animation
animate_clt(num_samples, sample_size, num_galaxies, num_dimensions)
