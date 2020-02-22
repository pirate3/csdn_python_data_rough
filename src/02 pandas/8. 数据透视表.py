# 以泰坦尼克号数据为例⼦进⾏展示
import numpy as np
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.shape)
print("-" * 30)

# 先进⾏粗分类
a = titanic.groupby("sex")[['survived']].mean()
# 可以看出，⼥性获救⽐例⼤概是男性的4倍多
print(a)
print("-" * 30)

# 尝试按sex，class分组，然后统计逃⽣⼈数，求mean后使⽤层级索引
# 可以清晰的展示出，逃⽣⼈数受sex，class 的影响
a = titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()
print(a)
print("-" * 30)

# pivot_table实现的效果等同于上⼀届的管道命令，是⼀个简写。
# 尝试按sex，class分组，然后统计逃⽣⼈数，求mean后使⽤层级索引
a = titanic.pivot_table('survived', index='sex', columns='class')
print(a)
print("-" * 30)

# 创建多级索引形状的DataFrame结果
# 按照sex，age，class统计，age分三个年龄段,0-18-80
# 使⽤cut函数对年龄进⾏分段
age = pd.cut(titanic['age'], [0, 18, 80])
a = titanic.pivot_table('survived', ['sex', age], 'class')
print(a)
print("-" * 30)

# 对列也可以使⽤类似策略
# 使⽤qcut对票价进⾏划分成两部分，每⼀部分⼈数相等
fare = pd.qcut(titanic['fare'], 2)
a = titanic.pivot_table('survived', ['sex', age], [fare, 'class'])
print(a)
