'''
误差线使⽤函数plt.errorbar来创建，可以使⽤不同的参数进⾏配置。
ecolor: 控制误差线颜⾊
fmt：线型，代码与plot线型控制参数⼀致
'''
import matplotlib.pyplot as plt
import numpy as np

# 基本误差线
x = np.linspace(0, 10, 50)
dy = x * 0.7

'''
y = np.sin(x) + dy
plt.errorbar(x, y, yerr=dy, fmt='.k', ecolor='blue')
'''

y = np.sin(x) + dy * np.random.rand(50)
plt.errorbar(x, y, yerr=dy, fmt='o', ecolor='blue', color='red', elinewidth=3, capsize=1)

plt.show()
