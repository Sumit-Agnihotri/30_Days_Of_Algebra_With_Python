import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-5, 5, 100)
y1 = 2*x_vals + 1
y2 = -x_vals + 4

plt.plot(x_vals, y1, label='y = 2x + 1')
plt.plot(x_vals, y2, label='y = -x + 4')
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid()
plt.title("Intersection of Two Linear Equations")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()