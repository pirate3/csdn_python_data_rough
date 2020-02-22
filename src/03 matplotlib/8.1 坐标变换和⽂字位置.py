'''
通过不同的坐标变换，可以把⽂字放在不同的位置，⽂字的坐标变换⽅法有：
ax.transData：以数据为基准的坐标变换
ax.transAxes： 以轴为基准
'''
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")
fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])

ax.text(1, 5, "Data:(1,5)", transform=ax.transData)
ax.text(0.5, 0.1, "Axes:(0.5, 0.1)", transform=ax.transAxes)

plt.show()
