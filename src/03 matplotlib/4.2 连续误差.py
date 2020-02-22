'''
连续误差表示的是连续量，没有⽐较合适的简单⽅法来绘制此类型图形，我们可以使⽤plt.plot和
plt.fill_between来解决，即画出两条区间线表示上下限，然后填充中间区域即可。
下⾯我们对sin和cos进⾏简单绘制，绘制后填充两个的中间差值。
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
ysin = np.sin(x)
ycos = np.cos(x)

plt.plot(x, ysin, color='red')
plt.plot(x, ycos, color='blue')
plt.fill_between(x, ysin, ycos, color='gray', alpha=0.2)

plt.show()