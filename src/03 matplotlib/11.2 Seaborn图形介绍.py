'''
Seaborn的主要思想是⽤ ⾼级命令 为统计数据探索和统计模型拟合创建各种图形
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['X', 'Y'])

sns.set()

### i直⽅图 ###
'''
for col in 'XY':
    plt.hist(data[col], alpha=0.5)
'''

# sns.kedplot可以实现KDE变量帆布的平滑估计
'''
for col in 'XY':
    sns.kdeplot(data[col], shade=True)
'''

# distplot可以让频次直⽅图和KDE结合起来
'''
sns.distplot(data['X'])
sns.distplot(data['Y'])
'''

# 如果是想kedplot输⼊的⼆维数据，则可以获得⼆维数据的可视化
'''
sns.kdeplot(data)
'''

# jointplot可以同时看到两个变量的联合分布和单变量的独⽴分布
'''
with sns.axes_style('white'):
    sns.jointplot('X', 'Y', data, kind='kde')
'''

# 向jointplot函数传递⼀些参数，可以⽤六边形块代替频次直⽅图。
'''
with sns.axes_style("white"):
    sns.jointplot('X', 'Y', data, kind='hex')
'''

### ii 矩阵图 ###
'''
对多维数据集进⾏可视化时，需要⽤到矩阵图（pair plot）来表示变量中任意两个变量的关系，探索多 维数据不同维度的相关性。
'''
'''

iris = sns.load_dataset('iris')
iris.head()

# 展示四个变量的矩阵
sns.pairplot(iris, hue='species', size=2.5)
'''

### iii. 分⾯频次直⽅图 ###
# 借助数据⼦集的频次直⽅图观察数据是⼀种很好的观察⽅法，下⾯案例展示的是服务员收取消费的数据。
'''
tips = sns.load_dataset('tips')
tips.head()
'''

'''
tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']
grid = sns.FacetGrid(tips, row='sex', col='time', margin_titles=True)
grid.map(plt.hist, 'tip_pct', bins=np.linspace(0, 40, 15))
'''

### iv. 因⼦图 ###
'''
with sns.axes_style(style='ticks'):
    g = sns.factorplot('day', 'total_bill', 'sex', data=tips, kind='box')
    g.set_axis_labels("Day", 'Total_bill')
'''

### v. 联合分布图 ###
# 可以⽤jointplot画出不同数据集的联合分布和各数据样本本身的分布。
# 联合分布图
'''
with sns.axes_style("white"):
    sns.jointplot('total_bill', 'tip', data=tips, kind='hex')
'''

# 带回归拟合的联合分布图
# 联合分布图⾃⾏进⾏kde和回归
'''
sns.jointplot('total_bill', 'tip', data=tips, kind='reg')
'''

### vi.条形图 ###
planets = sns.load_dataset('planets')
planets.head()

'''
with sns.axes_style("white"):
    g = sns.factorplot('year', data=planets, aspect=2, kind='count', color='steelblue')
    g.set_xticklabels(step=5)
'''

# 对⽐⽤不同的⽅法发现⾏星数量
with sns.axes_style("white"):
    g = sns.factorplot('year', data=planets, aspect=4.0, kind='count', hue='method', order=range(2001, 2015))
    g.set_ylabels('Number of Planets Discovered')

plt.show()
