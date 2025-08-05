import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-2, 6, 400)
y_vals = x_vals**2 - 5*x_vals + 6

plt.plot(x_vals, y_vals, label="y = x² - 5x + 6")
plt.axhline(0, color='black', lw=0.8)
plt.fill_between(x_vals, y_vals, where=(y_vals > 0), color='orange', alpha=0.3, label='y > 0')
plt.grid(True)
plt.legend()
plt.title("Graph of y = x² - 5x + 6")
plt.xlabel("x")
plt.ylabel("y")
plt.show()