'''
变形可以通过reshape来进⾏操作，前提是必须前后⻓度⼀致
也可以通过newaxis关键字来完成
newaxis是⼀个NoneType的内容，其实就是None
⼀般⽤来标识⼀给新的维度，⽐如1维的数组想变形成⼆维的，需要单纯的增加⼀个维度
⽐如 shape=(3,) ==> shape=(3,1)
'''
import numpy as np

# newaxis 是单纯的增加⼀个维度，加到行或加到列
a = np.arange(10)
print("a = ", a)
print("a.shape = ", a.shape)

# 获得⼀个⾏向量
a1 = a[np.newaxis, :]
print("a1 = ", a1)
print("a1.shape = ", a1.shape)

# 获得⼀个列向量
a2 = a[:, np.newaxis]
print("a2 = ", a2)
print("a2.shape = ", a2.shape)

'''
a =  [0 1 2 3 4 5 6 7 8 9]
a.shape =  (10,) 1维 10个元素
a1 =  [[0 1 2 3 4 5 6 7 8 9]]
a1.shape =  (1, 10) 2维
a2 =  [[0]
 [1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
a2.shape =  (10, 1)

'''