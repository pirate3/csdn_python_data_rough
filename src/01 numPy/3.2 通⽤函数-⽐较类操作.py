'''
此类⽐较操作也是逐个元素操作，最后的结果是⼀个包含布尔值的数组
此类操作包含：
==: np.equal
!=: no.not_equal
<: np.less
<=: np.less_equal
>: np.greater
>=: np.greater_equal
'''
import numpy as np

# 常⽤的np关于⽐较运算的操作
a = np.random.randint(100, size=(2, 5))
print("a = \n", a)
print()

# count_nonzero⽤来统计⾮零的值个数
# 统计⼩于50的数字的个数
print("⼩于50的格式总共 {}个".format(np.count_nonzero(a < 50)))
# 布尔值也可以作为数字运算，所以可以直接求和
# 统计⼤于50的数字的个数
print("⼤于50的个数总共 {}个".format(np.sum(a > 50)))

'''
a = 
 [[73 71 64 75 74]
 [53 14 55 10 73]]

⼩于50的个数总共 2个

⼤于50的个数总共 5个
'''

# 如果检测结果是否包含真值或者全部是否都是某个值
# 可以⽤any或者all
a = np.array([1, 2, 3, 4, 5, 6])
print("a = ", a)
print("a中包含⼤于10的数字吗：", np.any(a > 10))
print("a中包含⼤于5的数字吗：", np.any(a > 5))
print("a中的数组都⼤于0吗：", np.all(a > 0))

'''
a =  [1 2 3 4 5 6]
a中包含⼤于10的数字吗： False
a中包含⼤于5的数字吗： True
a中的数组都⼤于0吗： True
'''