"""
plt.subplot可以创建整⻬排列的⼦图，这个函数有三个整形参数：
⼦图⾏数
⼦图列数
索引值： 索引值从1开始，左上⻆到右下⻆逐渐增⼤
"""

import matplotlib.pyplot as plt
import numpy as np

'''
# matlab⻛格
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')
'''

# ⾯向对象⻛格
# plt.subplots_adjust调整⼦图间隔
# plt.add_subplot
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

plt.show()
