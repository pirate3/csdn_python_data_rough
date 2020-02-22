'''
借助于matplotlib⾃带的mplot3d包，我们可以实现三维图的绘制。

三维数据主要研究的是 z=f(x,y) , 如果绘制三维图形，需要有x，y，z，求三个数据然后在相应的点上
画点或者连线。
使⽤的画点或者连线的函数常⽤的是 ax.plot3d 和 ax.scatter3D 。
为了呈现更好的三维效果，默认散点图会⾃动改变透明度。
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

# 数据准备
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

# 三维线
ax.plot3D(x, y, z, 'red')

# 三维点
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

plt.show()
