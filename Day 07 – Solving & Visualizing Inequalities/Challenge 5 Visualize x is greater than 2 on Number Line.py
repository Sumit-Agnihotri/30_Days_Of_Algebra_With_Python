import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = x > 2

plt.axhline(0, color='gray')
plt.plot(x, y, label='x > 2')
plt.fill_between(x, 0, 1, where=(x > 2), color='skyblue', alpha=0.5)
plt.title('x > 2')
plt.yticks([])
plt.xlabel('x')
plt.legend()
plt.grid()
plt.show()