import matplotlib.pyplot as plt
import numpy as np

# 设置⻛格
plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 30)
y = np.sin(x)

rng = np.random.RandomState(0)
for marker in ['o', '.', 'x', '+', '^', '<', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker, label='marker={}'.format(marker))

plt.legend(numpoints=1)

plt.xlim(0, 1.8)

plt.show()