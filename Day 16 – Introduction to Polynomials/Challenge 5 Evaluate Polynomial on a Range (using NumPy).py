import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify, Poly, symbols

x = symbols('x')
poly = Poly(3*x**2 + 2*x - 5)
f = lambdify(x, poly.as_expr(), 'numpy')
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='P(x) = 3x² + 2x - 5')
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("Polynomial Plot")
plt.legend()
plt.show()