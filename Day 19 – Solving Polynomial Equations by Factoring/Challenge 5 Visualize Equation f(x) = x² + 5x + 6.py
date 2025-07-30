from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify

x = symbols('x')
f = x**2 + 5*x + 6
f_lambdified = lambdify(x, f, 'numpy')

x_vals = np.linspace(-10, 2, 400)
y_vals = f_lambdified(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = x² + 5x + 6')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("Roots of f(x) = x² + 5x + 6")
plt.scatter([-3, -2], [0, 0], color='red', zorder=5, label='Roots')
plt.grid()
plt.legend()
plt.show()