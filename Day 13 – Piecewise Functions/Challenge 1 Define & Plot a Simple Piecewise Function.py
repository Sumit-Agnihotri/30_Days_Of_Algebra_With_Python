# challenge1_basic_piecewise.py
import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-10, 10, 400)
f = lambda x: np.where(x < 0, x**2, x + 2)

plt.plot(x_vals, f(x_vals), label='Piecewise: x² if x<0 else x+2')
plt.title("Basic Piecewise Function")
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()