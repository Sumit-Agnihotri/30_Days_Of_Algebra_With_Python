import matplotlib.pyplot as plt
import numpy as np

a, b, c = 1, -3, 2  # Change these values to test other cases
f = lambda x: a*x**2 + b*x + c

x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label=f"y = {a}x² + {b}x + {c}")
plt.axhline(0, color='black', lw=0.8)
plt.title("Quadratic Graph – Root Behavior")
plt.grid(True)
plt.legend()
plt.show()