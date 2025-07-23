import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-10, 10, 400)
f = lambda x: x**2

plt.plot(x_vals, f(x_vals), label='f(x) = x²')
plt.plot(x_vals, 2 * f(x_vals), label='2*f(x) (Vertical Stretch)')
plt.plot(x_vals, 0.5 * f(x_vals), label='0.5*f(x) (Vertical Compression)')
plt.title("Stretch & Compression")
plt.grid()
plt.legend()
plt.show()