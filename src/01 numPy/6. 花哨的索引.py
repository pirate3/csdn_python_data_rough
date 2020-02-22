# 花哨的索引还可以有更花哨的⽤法
import numpy as np

x = np.arange(20).reshape((4, 5))
print("x = ", x)
print("x.shape = ", x.shape)
print()

# 1. 简单的索引和花哨的索引组合使⽤你
a = x[2, [3, 2, 1]]
print("x[2, [3,2,1]] = ", a)
print("a.shape = ", a.shape)

'''
x =  [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
x.shape =  (4, 5)

x[2, [3,2,1]] =  [13 12 11]
a.shape =  (3,)
'''

# 2, 花哨的索引+切⽚配合服⽤
print()
b = x[2:, [3, 2, 1]]
print("x[2:, [3,2,1]] = ", b)
print("b.shape = ", b.shape)

# 3. 花哨的索引+掩码
print(x)
mask = np.array([1, 0, 1, 1, 0], dtype=bool)
print(mask)
c = x[[0, 2, 3], mask]
print("x[[0,2,3], mask] = \n", c)
print("c.shape = ", c.shape)

# 利⽤花哨的索引批量修改数据
x = np.arange(10)
x[[2, 4, 6, 8]] = 999
print(x)
