# 设置环境
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

# 使⽤默认配置显示图形
x = np.random.randn(1000)
plt.hist(x)

# 保存默认的配置，修改后需要还原
rc_default = plt.rcParams.copy()
from matplotlib import cycler

colors = cycler('color', ['#777777', '#888888', '#999999', '#AAAAAA', '#BBBBBB', '#CCCCCC'])
plt.rc('axes', facecolor='#EEEEEE', edgecolor='none', axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='green')
plt.rc('lines', linewidth=2)
plt.hist(x)

for i in range(4):
    plt.plot(np.random.rand(10))

plt.rcParams.update(rc_default)

plt.show()