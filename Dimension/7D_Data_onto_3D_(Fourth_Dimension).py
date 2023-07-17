import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random 7D data
np.random.seed(42)
num_samples = 100
data_7d = np.random.rand(num_samples, 7)

# Function to project 7D data onto 3D using PCA
def project_7d_to_3d(data_7d):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=3)
    return pca.fit_transform(data_7d)

# Create the plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.axis('off')

# Project 7D data to 3D
projected_data_3d = project_7d_to_3d(data_7d)

# Scatter plot with colors representing the additional dimensions (4th, 5th, 6th, and 7th)
sc = ax.scatter(projected_data_3d[:, 0], projected_data_3d[:, 1], projected_data_3d[:, 2],
                s=100, c=data_7d[:, 3], cmap='viridis')

# Add a color bar for the 4th dimension
cbar = fig.colorbar(sc, ax=ax, shrink=0.8)
cbar.set_label('Fourth Dimension')

# Display the plot
plt.show()
