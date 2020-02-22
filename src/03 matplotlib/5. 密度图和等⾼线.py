'''
等⾼线或者密度图使我们常⽤图形， Matplotlib提供三个函数来供我们使⽤：
plt.contour: 等⾼线
plt.contourf: ⾃带填充⾊
plt.imshow： 显示图形
'''
import matplotlib.pyplot as plt
import numpy as np

# 设置⻛格
plt.style.use('seaborn-whitegrid')

'''
我们需要⼀个三维函数，z=f(x,y)来演示等⾼线图，按照下⾯函数来进⾏⽣成.
contour创建需要⾄少三个参数，x，y和z，其中x，y我们可以⽤横轴纵轴表示，z⽤等⾼线来表示就可
以。当只有⼀个颜⾊的图形是，虚线表示负值，实现部分表示正值。
我们使⽤meshgrid来从⼀维数据构成⼆维⽹格数据。
'''


# 函数
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

# 得到⽹格点矩阵
x, y = np.meshgrid(x, y)

# 计算z轴的值
z = f(x, y)

# 绘制图形
# plt.contour(x, y, z, colors='green')

# 绘制图形
# 使⽤红灰⾊配⾊⽅案
# 把值范围50等分
# plt.contour(x, y, z, 50, cmap='RdGy')

'''
以上绘图还是存在⽐如间隙过⼤的问题，我们可以⽤连续的颜⾊来填充图形，让它变的平滑起来。
plt.contourf可以满⾜我们的需求，其余填充参数基本同plt.contour⼀致。
'''

# 绘制图形
# 平滑过度⾊彩
# plt.contourf(x, y, z, 50, cmap='RdGy')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
上述图形的显示⾊彩过度还是不够细腻，因为画上⾯的图的时候使⽤的是⼀条⼀条的线来绘制，虽然可
以通过缩⼩间隙来让图形更加细腻，但是这样会造成计算资源的过度浪费，Matplotlib为我们提供了
imshow来完成渐变图的渲染。
plt.imshow函数不⽀持x，y轴的设置，必须通过extent参数来完成设置，extent=[xmin, xmax,
ymin, ymax]
plt.imshow默认以右上⻆为坐标原点，⼀般我们使⽤左下⻆为坐标原点
plt.imshow⾃动调整坐标轴精度来适配数据显示，可以通过plt.axis(aspect='image')来设置x，y的
单位
'''
# imshow

'''
plt.imshow(z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image')
'''

# 显示等⾼线的同时通过颜⾊显示内容
contours = plt.contour(x, y, z, 3, colors="green")
plt.clabel(contours, inline=True, fontsize=8)
plt.imshow(z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha=0.2)
plt.colorbar()
plt.axis(aspect='image')

plt.show()
