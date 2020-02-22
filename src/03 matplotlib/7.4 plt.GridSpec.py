'''
利⽤plt.GridSpec可以⽤来实现更复杂的多⾏多列⼦图⽹格。这种画图⽅式跟前端⽹⻚技术的⽹格思想
类似，需先⽤
plt.GridSpec指出需要总共划分的⾏和列，然后在具体的画相应⼦图的时候指出⼀个⼦图需要占⽤的⽹
格。
'''
import matplotlib.pyplot as plt
import numpy as np

'''
# 画图⽅式
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])
'''

# 正态分布数据的多⼦图显示
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# 设置坐标轴和⽹格配置
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)

main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# 主轴坐标画散点图
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# 次轴坐标画直⽅图
x_hist.hist(x, 40, histtype='stepfilled', orientation='vertical', color='red')
x_hist.invert_yaxis()

y_hist.hist(x, 40, histtype='stepfilled', orientation='horizontal',
            color='blue')
x_hist.invert_xaxis()

plt.show()
