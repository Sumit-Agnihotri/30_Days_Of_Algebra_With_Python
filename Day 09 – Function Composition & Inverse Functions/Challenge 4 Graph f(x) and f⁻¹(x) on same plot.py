import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-10, 10, 100)
f_vals = 2 * x_vals + 3
f_inv_vals = (x_vals - 3) / 2

plt.plot(x_vals, f_vals, label='f(x) = 2x + 3', color='blue')
plt.plot(x_vals, f_inv_vals, label='f⁻¹(x) = (x - 3)/2', color='green')
plt.plot(x_vals, x_vals, '--', color='gray', label='y = x')

plt.title("Function and its Inverse")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.show()