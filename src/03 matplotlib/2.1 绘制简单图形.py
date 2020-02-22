import matplotlib.pyplot as plt
import numpy as np

# 图形显示⻛格
plt.style.use('seaborn-whitegrid')

# 创建fig和ax
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 100)

'''
# 显示sin函数图形
plt.plot(x, np.sin(x))
# 显示cos函数图形
plt.plot(x, np.cos(x))
'''

# 2.2 调整图形⻛格
# 不同颜⾊的线条
'''
plt.plot(x, np.sin(x-1), color='black')
plt.plot(x, np.sin(x-2), color='y')
plt.plot(x, np.sin(x-3), color='0.65')
plt.plot(x, np.sin(x-4), color='#FF0000')
plt.plot(x, np.sin(x-5), color=(0.2, 1.0, 1.0))
plt.plot(x, np.sin(x-6), color='chartreuse')
'''

'''
同样，使⽤linestyle参数可以定制图形中线的特征，常⽤的linestyle值为：
solic： 实现，会⽤ - 做简写
dashed：虚线，⽤ -- 做简写
dashdot：点划线， ⽤ -. 简写
dotted：实⼼点线， ⽤ ： 简写
'''

# 不同颜⾊的线条
'''
plt.plot(x, np.sin(x - 1), linestyle='solid', color='black')
plt.plot(x, np.sin(x - 2), linestyle='--', color='y')
plt.plot(x, np.sin(x - 3), linestyle='dashdot', color='0.65')
plt.plot(x, np.sin(x - 4), linestyle=':', color='#FF0000')
'''

# 使⽤组合简写 linestyle和color可以组合在⼀起使⽤更简洁的表示形式
plt.plot(x, x + 0, '-r')
plt.plot(x, x + 1, '--g')
plt.plot(x, x + 2, '-.b')
plt.plot(x, x + 3, ':c')

# ⼿动设置坐标轴
plt.xlim(-5, 10)
plt.ylim(-3, 5)

plt.axis([-5, 10, -3, 5])
plt.axis('tight')  # 图形空⽩⾃动去掉
plt.axis('equal')  # 显示分辨率1:1


plt.show()
