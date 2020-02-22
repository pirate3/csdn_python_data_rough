'''
常⻅的算数运算操作如下：
+：np.add
-: np.subtract
-: np.negative
*: np.multiply
/: np.divide
//: np.floor_divide
**: np.power
%: np.mod
absolute(abs):绝对值，⽐较特殊，可以处理复数，当求复数的绝对值的时候，结果是复数的幅度
'''
import numpy as np

# 运算符举例
# 需要注意的是逐个元素运算
a = np.arange(20).reshape([4, 5])
print("a = \n", a)
print("a+3 = \n", a + 3)
print("a//5 = \n", a // 3)
print("a**2 = \n", a ** 2)
print("-a = \n", -a)
print("a % 3 = \n", a % 3)

'''
a = 
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
a+3 = 
 [[ 3  4  5  6  7]
 [ 8  9 10 11 12]
 [13 14 15 16 17]
 [18 19 20 21 22]]
a//5 = 
 [[0 0 0 1 1]
 [1 2 2 2 3]
 [3 3 4 4 4]
 [5 5 5 6 6]]
a**2 = 
 [[  0   1   4   9  16]
 [ 25  36  49  64  81]
 [100 121 144 169 196]
 [225 256 289 324 361]]
-a = 
 [[  0  -1  -2  -3  -4]
 [ -5  -6  -7  -8  -9]
 [-10 -11 -12 -13 -14]
 [-15 -16 -17 -18 -19]]
a % 3 = 
 [[0 1 2 0 1]
 [2 0 1 2 0]
 [1 2 0 1 2]
 [0 1 2 0 1]]
'''

# 三⻆函数举例
theta = np.linspace(0, np.pi, 5)
print("theta = ", theta)
# 三⻆函数
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))
# 反三⻆函数
print("arcsin(theta) = ", np.arcsin(theta))
print("arccos(theta) = ", np.arccos(theta))
print("arctan(theta) = ", np.arctan(theta))

# 指数和对数函数常⽤的是以e, 2, 10为底的运算，同样对于⾮常⼩的值输⼊，numpy也给出了精度好的运算⽅式。
a = np.array([1, 2, 3])
print("a = ", a)
print("e^a = ", np.exp(a))
print("2^a = ", np.exp2(a))
# 直接使⽤power函数进⾏操作
print("3^a = ", np.power(3, a))
print("ln(a) = ", np.log(a))
print("log2(a) = ", np.log2(a))
print("log10(a) = ", np.log10(a))

# 以下特殊的版本，对⾮常⼩的输⼊值，能保持⽐较好的精度。
# 在Python NumPy中以自然数为底的指数计算方法为exp，expm1用来计算exp(x)-1，输入可以是普通数字也可以是数组。
a = np.array([0, 0.001, 0.01, 0.1])
print("exp(a) - 1 = ", np.expm1(a))
print("log(1+x) = ", np.log1p(a))

# 对exp和expm1在极⼩数值上的⽐较
print("expm1 = ", np.expm1(1e-10))
print("exp-1 = ", np.exp(1e-10) - 1)
# log1p和log(1+x)的⽐较
print("log1p = ", np.log1p(1e-99))
print("log(1+x) = ", np.log(1 + 1e-99))
