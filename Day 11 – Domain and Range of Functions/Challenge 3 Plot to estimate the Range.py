import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-10, 10, 400)
y_vals = 1 / (x_vals - 2)

plt.plot(x_vals, y_vals)
plt.title("f(x) = 1 / (x - 2)")
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(2, color='red', linestyle='--', label='x = 2 (undefined)')
plt.ylim(-20, 20)
plt.legend()
plt.show()