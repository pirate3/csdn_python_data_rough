'''
默认快排, 其他归并排序，堆排序， 稳定排序
不修改源数据，返回排好的数据下使⽤np.sort(data)
修改数据源，使⽤ data.sort()
'''
import numpy as np

x = np.random.randint(20, size =10)
print("排序前 X = ", x)
a = np.sort(x)
print("排序后 X = ", x)
print("排序后 a = ", a)
x.sort()
print("修改数据源排序后 X = ", x)