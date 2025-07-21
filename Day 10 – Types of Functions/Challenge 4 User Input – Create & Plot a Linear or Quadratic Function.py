import matplotlib.pyplot as plt
import numpy as np

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter constant c: "))

x_vals = np.linspace(-10, 10, 400)
y_vals = a * x_vals**2 + b * x_vals + c

plt.plot(x_vals, y_vals, label=f"f(x) = {a}x² + {b}x + {c}")
plt.title("Your Custom Quadratic Function")
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()