import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-10, 10, 400)
f = lambda x: x**2
transformed = lambda x: -2 * (x + 1)**2 + 4

plt.plot(x_vals, f(x_vals), label='f(x) = x²')
plt.plot(x_vals, transformed(x_vals), label='Transformed: -2(x + 1)² + 4')
plt.title("Combined Transformation")
plt.grid()
plt.legend()
plt.show()