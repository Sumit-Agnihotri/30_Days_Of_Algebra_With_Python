import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace

x_values = np.linspace(-10, 10, 400)
f = lambda x: x**2

plt.plot(x_values, f(x_values), label='f(x) = x²')
plt.plot(x_values, f(x_values) + 3, label='f(x) + 3 (Shift Up)')
plt.plot(x_values, f(x_values) - 3, label='f(x) - 3 (Shift Down)')
plt.title("Vertical Shifts")
plt.grid()
plt.legend()
plt.show()