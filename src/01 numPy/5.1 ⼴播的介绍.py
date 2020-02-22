'''
⼴播允许对不同⼤⼩的数组进⾏操作，例如前⾯介绍的⼀个标量和⼀个数组相加，这种⾃动把⾃⼰编程
和对⽅形状⼀样然后进⾏
操作的能⼒，叫⼴播。
'''
import numpy as np

a = np.zeros(5)
print("a = ", a)
# 我们可以认为是 a + 4 = array(0,0,0,0,0) + array(4,4,4,4,4)
# 此时标量4⾃动扩展成了 array(4,4,4,4,4)
b = a + 4
print("b = ", b)

'''
a =  [0. 0. 0. 0. 0.]
b =  [4. 4. 4. 4. 4.]
'''

a = np.arange(5)
print("a = ", a)
print()
b = np.arange(15).reshape((3, 5))
print("b = \n", b)
print()
# 此处相当于把b按⾏扩展成了⼀个 3x5的数组，然后和a进⾏bitwise的相加
c = a + b
print("c = \n", c)

'''
a =  [0 1 2 3 4]

b = 
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

c = 
 [[ 0  2  4  6  8]
 [ 5  7  9 11 13]
 [10 12 14 16 18]]
'''

print("-" * 30)
# 负责例⼦，需要两边⼴播
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
c = a + b
print("a = \n", a)
print()
print("b = \n", b)
print()
print("c = \n", a + b)

'''
a = 
 [0 1 2]

b = 
 [[0]
 [1]
 [2]]

c = 
 [[0 1 2]
 [1 2 3]
 [2 3 4]]

'''
