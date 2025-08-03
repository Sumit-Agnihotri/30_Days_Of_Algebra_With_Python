import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 400)
y1 = 10 - x
y2 = np.zeros_like(x)

plt.plot(x, y1, label='x + y ≤ 10')
plt.fill_between(x, y2, y1, color='lightblue', alpha=0.5)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Feasible Region Bounded by x+y≤10, x≥0, y≥0")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()