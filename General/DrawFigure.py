import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x**2 
plt.figure(figsize=(5, 2))
plt.plot(x, y)

plt.title('Plot of y = x^2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()