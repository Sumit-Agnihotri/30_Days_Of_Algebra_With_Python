import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-2, 6, 400)
y1 = 2*x_vals - 1
y2 = -x_vals + 4

plt.plot(x_vals, y1, label="y = 2x - 1")
plt.plot(x_vals, y2, label="y = -x + 4")
plt.fill_between(x_vals, y1, y2, where=(y1 <= y2), color='lightgreen', alpha=0.4)

plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True)
plt.legend()
plt.title("Feasible Region for System of Inequalities")
plt.xlabel("x")
plt.ylabel("y")
plt.show()