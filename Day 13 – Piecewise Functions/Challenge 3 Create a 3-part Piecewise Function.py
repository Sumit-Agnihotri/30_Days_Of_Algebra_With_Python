import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-10, 10, 500)

def custom_piecewise(x):
    return np.piecewise(x, 
                        [x < -2, (x >= -2) & (x < 3), x >= 3], 
                        [lambda x: x**2,
                         lambda x: x + 4,
                         lambda x: 2*x - 1])

y_vals = custom_piecewise(x_vals)

plt.plot(x_vals, y_vals, label='3-Part Piecewise')
plt.title("Custom 3-Part Function")
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()