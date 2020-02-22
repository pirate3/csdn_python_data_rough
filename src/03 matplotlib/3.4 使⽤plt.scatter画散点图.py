'''
另⼀个画散点图的函数是scatter，⽤法和plot函数类似。
但scatter更加灵活，甚⾄可以单独控制每个散点不同的属性，例如⼤⼩，颜⾊，边控等。
相对来讲，对于⼤量数据的渲染，plot效率要⾼于scatter。

'''

# scatter案例
from pandas import np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.4, cmap='viridis')

# 显示颜⾊条
plt.colorbar()

plt.show()
