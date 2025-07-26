import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-5, 10, 500)
mask = (x_vals > 1) & (x_vals < 5)

plt.plot(x_vals, [0]*len(x_vals), 'k--')
plt.fill_between(x_vals, 0, 1, where=mask, color='skyblue', label='|x - 3| < 2')
plt.title("Solution Set for |x - 3| < 2")
plt.yticks([])
plt.xlabel("x")
plt.legend()
plt.grid()
plt.show()