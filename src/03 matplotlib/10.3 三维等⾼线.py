'''
三维图默认的观察视⻆可能不是最后的，我们可以时候⽤ ax.view_init 来改变观察视⻆，两个参数：
俯仰⻆度，即x-y平⾯的旋转⻆度
⽅位⻆度，即沿着z轴顺时针转动⻆度
'''
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax.contour3D(X, Y, Z, 50)

ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")


# 上图调整旋转⻆度为（60， 30）
ax.view_init(60, 30)

plt.show()
