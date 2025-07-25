import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-5, 10, 500)
y_vals = x_vals + 2

plt.plot(x_vals, y_vals, label='y = x + 2')
plt.fill_between(x_vals, y_vals, 10, where=(y_vals < 10), color='lightblue', alpha=0.5)
plt.axhline(10, color='red', linestyle='--', label='y = 10')
plt.title("Shaded Region: y < 10")
plt.grid()
plt.legend()
plt.show()