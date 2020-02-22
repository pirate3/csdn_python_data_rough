'''
使⽤plt.hist可以画直⽅图，重要的参数有：
bins: 画⼏条⽅图
color: 颜⾊
alpha: 透明度
histtype: 图类型
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# 设置⻛格
plt.style.use('seaborn-whitegrid')

# 更复杂的案例
'''
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
'''

# ii. ⼆维频次直⽅图和数据区间划分
# 准备数据
mean = [0, 0]
cov = [[1, 1], [1, 2]]

# 多元正太分布随机样本抽取
# mean:多元正态分布的维度
# cov:多元正态分布的协⽅差矩阵，且协⽅差矩阵必须是对称矩阵和半正定矩阵(形状为(N,N)的⼆维数组)。
# size: 数组的形状（整数或者由整数构成的元组）。如果该值未给定，则返回单个N维的样本（N恰恰是上⾯mean的⻓度）。
x, y = np.random.multivariate_normal(mean, cov, 10000).T

# 使⽤plt.hist2d可以画⼆维直⽅图。
'''
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label("counts in bin")
'''

# hist2d是⽤的⽅块组成的图形，还可以使⽤六边形进⾏图形分割，需要使⽤plt.hexbin来完成，⽤来将
# 图形化成六⻆形的蜂窝。
'''
plt.hexbin(x, y, gridsize=30, color='red')
cb = plt.colorbar(label="count in bin")
'''

# 核密度估计(KernelDensityEstimation)是⼀种常⽤的评估多维度分布密度的⽅法， 本节主要是对画图函
# 数做⼀个展示，不详细讲述kde算法。
# kde⽅法通过不同的平滑带宽⻓度在拟合函数的准确性和平滑性之间做出⼀种权衡。
data = np.vstack([x, y])
kde = gaussian_kde(data)

x = np.linspace(-3.5, 3.5, 40)
y = np.linspace(-6, 6, 40)

x, y = np.meshgrid(x, y)
z = kde.evaluate(np.vstack([x.ravel(), y.ravel()]))

plt.imshow(z.reshape(x.shape), origin='lower', aspect='auto', extent=[-3.5, 3.5, -6, 6], cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")

plt.show()
