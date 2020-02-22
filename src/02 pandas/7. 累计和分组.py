'''
sum： 求和
mean：平均数
median：中位数
min：最⼩值
max：最⼤值
count：计数
first/last: 第⼀项和最后⼀项
std: 标准差
var：⽅差
mad：均值绝对⽅差
prod：所有项乘积
'''

# 我们这次准备数据时候⽤seaborn提供的⾏星数据，包括天⽂学家观测到的围绕恒星运⾏的⾏星数据
# 下载地址：
# https://github.com/mwaskom/seaborn-data
import seaborn as sns

planets = sns.load_dataset('planets')
print(planets.shape)
# 显示数据头部
print(planets.head())
