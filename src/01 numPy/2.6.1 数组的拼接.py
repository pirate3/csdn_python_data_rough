'''
numpy.concatenate: 可以指明拼接的轴
numpy.hstack: 沿着横轴进⾏拼接
numpy.vstack: 沿着竖轴进⾏拼接
numpy.dstack: 沿着第三个轴进⾏拼接
'''
import numpy as np

# 同样，concatenate可以对多维数组进⾏拼接
# 拼接的时候，往往需要指出沿着哪个轴或者维度进⾏拼接
a1 = np.arange(12).reshape((3, 4))
print("a1 = \n", a1)
a2 = np.arange(100, 112).reshape((3, 4))
print("a2 = \n", a2)
# 此时明显看出concatenate默认是沿着第⼀个轴（index=0）拼接
a3 = np.concatenate([a1, a2])
print("a3 = \n", a3)
# 如果有必要，需要指明进⾏拼接的轴
# 下⾯案例沿着第⼆个轴进⾏拼接，index=1
a4 = np.concatenate([a1, a2], axis=1)
print("a4 = \n", a4)

'''
a1 = 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
a2 = 
 [[100 101 102 103]
 [104 105 106 107]
 [108 109 110 111]]
a3 = 
 [[  0   1   2   3]
 [  4   5   6   7]
 [  8   9  10  11]
 [100 101 102 103]
 [104 105 106 107]
 [108 109 110 111]]
a4 = 
 [[  0   1   2   3 100 101 102 103]
 [  4   5   6   7 104 105 106 107]
 [  8   9  10  11 108 109 110 111]]
'''

# vstack & hstack
a1 = np.arange(4).reshape((1,4))
a2 = np.arange(100,112).reshape((3,4))
a3 = np.arange(10,13).reshape((3, 1))

# 注意vstack参数的shape
a4 = np.vstack([a1, a2])
print("a4 = \n", a4)
a5 = np.hstack([a2, a3])
print("a5 = \n", a5)

'''
a4 = 
 [[  0   1   2   3]
 [100 101 102 103]
 [104 105 106 107]
 [108 109 110 111]]
a5 = 
 [[100 101 102 103  10]
 [104 105 106 107  11]
 [108 109 110 111  12]]
'''