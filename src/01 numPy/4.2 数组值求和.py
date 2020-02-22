'''
numpy.sum函数和python的求和函数功能基本⼀致,但是还是有⼀些⼩区别:
numpy的求和函数具有维度的概念，求和多项可以是数组
同时参数含义跟python的sum并不⼀致
numpy.sum速度快⼀些
'''
from numpy import np

a = np.arange(100).reshape((10,10))
b = np.sum(a)
print(b)