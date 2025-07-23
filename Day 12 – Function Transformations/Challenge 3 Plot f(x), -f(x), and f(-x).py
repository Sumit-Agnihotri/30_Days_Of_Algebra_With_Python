import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-10, 10, 400)
f = lambda x: x**2

plt.plot(x_vals, f(x_vals), label='f(x) = x²')
plt.plot(x_vals, -f(x_vals), label='-f(x) (Reflect over x-axis)')
plt.plot(x_vals, f(-x_vals), label='f(-x) (Reflect over y-axis)')
plt.title("Reflections")
plt.grid()
plt.legend()
plt.show()