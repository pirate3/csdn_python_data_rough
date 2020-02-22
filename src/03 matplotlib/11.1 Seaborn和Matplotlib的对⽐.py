import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use("classic")

# 准备数据
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# matplotlib画图
'''
plt.plot(x, y)
plt.legend("ABCDEF", ncol=2, loc='upper left')
'''

# seaborn画图
sns.set()  # 多此一行
plt.plot(x, y)
plt.legend("ABCDEF", ncol=2, loc='upper left')

plt.show()
