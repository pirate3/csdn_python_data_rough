'''
对于⼀些要求均匀采样的⽹格数据显得太过严格⽽不太容易实现的图像，我们可以使⽤三⻆剖分
(triangulation-based plot)来解决。
'''
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


fig = plt.figure()
ax = plt.axes(projection='3d')

theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)

# 随机散点数据组成的图形
'''
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=1)
ax.view_init(60, 30)
'''

# 随机数据构成三⻆剖分
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
ax.view_init(60, 30)

plt.show()
