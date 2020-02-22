'''
通过组合使⽤⽐较类运算，可以快速提取出符合条件的数值，此类操作称为掩码操作。
'''
import numpy as np

a = np.random.randint(100, size=(3,5))
print("a = \n", a)
print()
# 掩码可以快速提取数据，⽐如，提取出⼩于50的数据
a1 = a[a<50]
print("a1 = ", a1)
print("a1.shape = ", a1.shape)

'''
a = 
 [[93 30 40 70 25]
 [64 37 82 24 11]
 [22 72 26 91  6]]

a1 =  [30 40 25 37 24 11 22 26  6]
a1.shape =  (9,)
'''