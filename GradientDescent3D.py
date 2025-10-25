import numpy as np
import matplotlib.pyplot as plt


def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5


def calculate_gradient(x,y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)

x= np.arange(-1,1,0.05)
y= np.arange(-1,1,0.05)

x, y = np.meshgrid(x,y)
z = z_function(x,y)

current_pos = (0.7, 0.4, z_function(0.7, 0.4))

learning_rate = 0.01
ax = plt.subplot(projection='3d', computed_zorder=False)

for _ in range(500):
    x_derivative, y_derivative = calculate_gradient(current_pos[0], current_pos[1])
    x_new, y_new = current_pos[0] - learning_rate * x_derivative, current_pos[1] - learning_rate * y_derivative
    current_pos = (x_new, y_new, z_function(x_new, y_new))
    ax.plot_surface(x, y, z, cmap='viridis',zorder=0)
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], color='magenta')
    plt.pause(0.001)
    ax.clear()
