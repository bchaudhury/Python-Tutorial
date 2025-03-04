import matplotlib.pyplot as plt
import numpy as np

# Create a simple plot 

# Create the x and y axis data
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# Plot the data

plt.plot(xpoints, ypoints)
plt.show()

# Create a plot with more points

ypoints = np.array([3, 8, 1, 10])

# Plot the data

plt.plot(ypoints, marker = 'o')
plt.show()