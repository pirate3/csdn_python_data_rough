import numpy as np

# 1. 使⽤字典作为机构化数组的类型
a = np.dtype({"names": ("name", "score", "heigh"), \
              "formats": ("U10", "i4", "f8")})
print(a)

# 2. 使⽤python数据类型或者NumPy的dtype类型
b = np.dtype({"names": ("name", "score", "heigh"), \
              "formats": ((np.str_, 10), int, float)})
print(b)

# 3. 如果类型的名称不重要， 可以省略
c = np.dtype("S10, i4, f8")
print(c)

# 4. 复合类型
# 定义⼀个结构
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (4, 4))])
# 利⽤定义的结构tp创建⼀份内容
x = np.zeros(2, dtype=tp)
# 打印整个内容
print(x)
# 只打印出数据内容
print(x['mat'][0])
