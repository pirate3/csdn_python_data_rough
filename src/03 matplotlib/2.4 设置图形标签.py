import matplotlib.pyplot as plt
import numpy as np

# 使⽤⾯向对象的⽅法画图
x = np.linspace(0, 10, 50)
fig, ax = plt.subplots()

#默认legend只显示有label的线条，没有的不显示
sin_line = ax.plot(x, np.sin(x), color='red', label="SIN")
#cos_line = ax.plot(x, np.cos(x), color='blue', label="COS")
cos_line = ax.plot(x, np.cos(x), color='blue')

# 全部使⽤默认
# ax.legend()

# 更改位置，添加边框
# ax.legend(loc='upper left', frameon=True)
# ax.legend(loc='upper left', frameon=True, shadow=True, framealpha=0.2)

# 明确把需要添加图例的线条放⼊legend作为参数
# 没有添加的不显示
#ax.legend(cos_line, loc='upper left', frameon=True, shadow=True, framealpha=0.2)

plt.show()
