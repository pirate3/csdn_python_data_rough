'''
可以通过cmap参数为图形设置颜⾊条的配置⽅案, 所有配⾊⽅案都在
plt.cm命名空间⾥，可以直接通过 plt.cm.<TAB> 查看。
选择合理的配⾊⽅案能让实⾏示例清晰明了，常⻅的配⾊⽅案有：
顺序配⾊⽅案： 由⼀组连续的颜⾊构成的⽅案，例如binary或者viridis
互逆配⾊⽅案： 由两种互补的颜⾊构成，表示正反两种含义，例如RdBu或者PuOr
定性配⾊⽅案：随机顺序的⼀组颜⾊，例如rainbow或者jet
'''

import matplotlib.pyplot as plt
from pandas import np

x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

# 使⽤灰⾊颜⾊条
# plt.imshow(I, cmap='RdBu')

# 1. 配⾊⽅案
# 2. 颜⾊多少等分
c = plt.cm.get_cmap("PuOr", 10)
plt.imshow(I, cmap=c)

plt.colorbar()
plt.show()
