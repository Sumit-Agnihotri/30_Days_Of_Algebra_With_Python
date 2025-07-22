from sympy import Abs, symbols, solveset, S
from sympy.calculus.util import continuous_domain

x = symbols('x')
f = Abs(x)
domain = continuous_domain(f, x, S.Reals)
print("Domain of f(x) = |x| is:", domain)

import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-10, 10, 400)
y_vals = np.abs(x_vals)

plt.plot(x_vals, y_vals)
plt.title("f(x) = |x|")
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.show()