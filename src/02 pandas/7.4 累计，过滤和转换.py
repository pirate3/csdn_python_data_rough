'''
GroupBy基本功能是分组，但分组之后相应的操作，也为数据分析提供了很多⾼效的⽅法。
此类⽅法⼤概分为：
aggregate：累计
filter：过滤
transform：变换
apply：应⽤
'''

# apply可以让⼈在每个数据上应⽤任意⽅法，这个函数让输⼊⼀个DataFrane，返回的结果可以是pandas对象或者
# 标量。

# 求每⼀项的百分⽐
from pandas.tests.groupby.test_value_counts import df


def norm_data_1(x):
 # 求百分⽐
 x['data_1'] = x['data_1'] / x['data_1'].sum()

 return x
rst = df.groupby('key').apply(norm_data_1)
print(rst)