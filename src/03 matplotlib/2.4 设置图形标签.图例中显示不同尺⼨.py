import matplotlib.pyplot as plt
import numpy as np

# scatter⽤来画散点图
# 我们将在后⾯章节中讲述
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

# 设定横轴坐标的范围
plt.xlim(-3, 6)

# 画散点图 cmap
plt.scatter(x, y, c=colors, s=sizes, alpha=0.4, cmap='viridis')

# 显示颜⾊条
plt.colorbar()

# 画图例散点图
for a in [0.1, 0.3, 0.5, 0.7, 0.9]:
    plt.scatter([], [], c='red', alpha=0.5, s=a * 300, label="{}Label".format(a))
    # 画图例⽂字
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Random Value')

plt.show()
