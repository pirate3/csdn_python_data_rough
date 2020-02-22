'''
numpy的聚合可以直接作⽤在数组上⾯，不需要每次都numpy.xxx调⽤。
同时⼀般如果名称相同功能也相同，相对速度⽐python同名功能要快。
numpy中可⽤的聚合函数如下，需要注意的是，除any和all之外，每个函数都存在⼀个NaN安全的版
本，形式是在函数名称前加nan,例如np.nansum就是sum的NaN安全版本：

np.sum: 和
np.prod: 积
np.mean: 平均数
np.std: 标准差
np.var: ⽅差
np.min: 最⼩值
np.max: 最⼤值
np.argin: 最⼩值的索引
np.argmax: 最⼤值的索引
np.median: 中位数
mp.oercentile: 基于元素排序的统计值
np.any: 是否⾄少存在⼀个为真的元素
np.all: 所有元素是否为真
'''