import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-10, 10, 400)
f = lambda x: x**2

plt.plot(x_vals, f(x_vals), label='f(x) = x²')
plt.plot(x_vals, f(x_vals - 2), label='f(x - 2) (Right Shift)')
plt.plot(x_vals, f(x_vals + 2), label='f(x + 2) (Left Shift)')
plt.title("Horizontal Shifts")
plt.grid()
plt.legend()
plt.show()