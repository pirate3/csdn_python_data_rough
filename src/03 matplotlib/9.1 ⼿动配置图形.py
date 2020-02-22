'''
通过⼿动配置图形，可以改变图形的刻度，北京等内容，下⾯例⼦是对图形配置的⼀个简单示例。
'''
# 设置环境
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

# 使⽤默认配置显示图形
x = np.random.randn(1000)
plt.hist(x)

# 对图形进⾏各种配置
ax = plt.axes()
ax.set_axisbelow(True)

# 被⾊⽹格线
plt.grid(color='g', linestyle='solid')

# 隐藏坐标的线条
for spine in ax.spines.values():
    spine.set_visible(False)

# 隐藏上边和右边的刻度
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# 弱化刻度和标签
ax.tick_params(colors='green', direction='out')
for tick in ax.get_xticklabels():
    tick.set_color('orange')
for tick in ax.get_yticklabels():
    tick.set_color('orange')

# 设置频次直⽅图轮廓⾊和填充⾊
ax.hist(x, edgecolor="#1122FF", color='#998877')

plt.show()
