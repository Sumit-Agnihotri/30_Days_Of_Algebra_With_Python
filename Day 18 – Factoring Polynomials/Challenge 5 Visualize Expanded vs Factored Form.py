from sympy import symbols, factor
import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify, factor

x = symbols('x')
expr = x**2 + 5*x + 6\

f_exp = lambdify(x, expr, 'numpy')
f_factored = lambdify(x, factor(expr), 'numpy')  # Should give same output

x_vals = np.linspace(-10, 5, 400)
plt.plot(x_vals, f_exp(x_vals), label='Original')
plt.plot(x_vals, f_factored(x_vals), '--', label='Factored (same curve)')
plt.axhline(0, color='black', lw=0.5)
plt.title("Factoring a Polynomial")
plt.grid()
plt.legend()
plt.show()