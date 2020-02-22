'''
np.random.randin()
ndim
'''

import numpy as np

# ⽣成三个数组
a1 = np.random.randint(100, size=10)  # 参数siz是⽣成数组的shape属性
a2 = np.random.randint(100, size=(4, 6))
a3 = np.random.randint(100, size=(2, 5, 6))

# 打印出数组a1, a2, a3的属性
for a in [a1, a2, a3]:
    print("dtype={}, ndim={}, shape={}, size={}, itemsize={}, nbytes={}".
          format(a.dtype, a.ndim, a.shape, a.size, a.itemsize, a.nbytes))

'''
dtype=int32, ndim=1, shape=(10,), size=10, itemsize=4, nbytes=40
dtype=int32, ndim=2, shape=(4, 6), size=24, itemsize=4, nbytes=96
dtype=int32, ndim=3, shape=(2, 5, 6), size=60, itemsize=4, nbytes=240
'''
