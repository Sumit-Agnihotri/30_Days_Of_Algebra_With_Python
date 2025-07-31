import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

t = symbols('t')
h = -5 * t**2 + 20 * t

t_vals = np.linspace(0, 5, 400)
f = lambdify(t, h, 'numpy')
h_vals = f(t_vals)

plt.plot(t_vals, h_vals, label='h(t) = -5t² + 20t')
plt.title("Ball Height Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.legend()
plt.show()