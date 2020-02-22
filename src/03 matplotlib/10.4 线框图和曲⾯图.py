'''


'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 线框图
'''
ax.plot_wireframe(X, Y, Z, color='red')
ax.set_title('wireframe')
ax.view_init(60, 30)
'''

# 线框图2
'''
ax.plot_surface(X, Y, Z, color='green')
ax.set_title('surface')
ax.view_init(60, 30)
'''

r = np.linspace(0, 6, 30)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)

X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.view_init(60, -40)

plt.show()
