'''
Matplotlib有默认的坐标轴定位器(locator)和格式⽣成器(formatter)，基本需求可以满⾜，但是如果需
要定制更细腻的表现，需要⽤到其他的东⻄。
Matplotlib画图的基本原理是：
figure对象可以看做是⼀个图形的总的容器，⾥⾯可以包含⼏个⼦图
axes：每个figure包含⼀个或者多个axes，每个axes有包含其他表示图形内容的对象
每个axes有xaxis和yaxis属性，每个属性包含坐标轴的线条，刻度，标签等属性
'''
import matplotlib.pyplot as plt
import numpy as np

# i. 主要刻度和次要刻度
# 主要和次要刻度标签都是通过LogLocater对象设置的， 同样格式⽣成器都是 LogFormatterSciNotaion对象。
ax = plt.axes(xscale='log', yscale='log')
print(ax.xaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())
print(ax.xaxis.get_major_formatter())
print(ax.xaxis.get_minor_formatter())

# ii. 隐藏刻度和标签
# 删除locator和formmater
ax = plt.axes()
ax.plot(np.random.rand(50))
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

# iii. 增减刻度数量
# ⼀下图例使⽤默认刻度，但显得过于拥挤
fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)

# iv. 花哨的刻度格式
# 使⽤MultipleLocator可以实现把刻度放在你提供的数值的倍数上。
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 100)
ax.plot(x, np.sin(x), lw=3, label='SIN')
ax.plot(x, np.cos(x), lw=3, label='COS')
# 设置⽹格，图例和坐标轴上下限
ax.grid(True)
ax.legend(frameon=False)
ax.axis('equal')
ax.set_xlim(0, 3 * np.pi)

#v. 定位器和格式⽣成器常⽤值
'''
定位器和格式⽣成器常⽤的取值在plt命名空间内可以找到，下⾯列出来：
NullLocator: ⽆刻度
FixedLocator：刻度位置固定
IndexLocator：⽤索引做定位器，例如x=range(10)
LinearLocator: 从min到max均匀分布
LogLocator: 从min到max对数分布
MultipleLocator： 刻度和范围是基数的倍数
MaxNLocator： 为最⼤刻度找到最优位置
AutoLocator： 以MaxNlocator进⾏简单配置
AutoMinorLocator：次要刻度的定位器

格式⽣成器的取值：
NullFormatter： 刻度上⽆标签
IndexFormatter： 将⼀组标签设置为字符串
FixedFormatter： ⼿动设置标签
FuncFormatter：⾃定义函数设置标签
FormatStrFormatter：为每个刻度设置字符串格式
ScalarFormatter： 为标量值设置标签
LogFormatter： 对数坐标轴的默认格式⽣成器
'''
