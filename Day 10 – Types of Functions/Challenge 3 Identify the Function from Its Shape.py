import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-10, 10, 400)
y_vals = np.abs(x_vals)

plt.plot(x_vals, y_vals)
plt.title("Guess This Function!")
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.show()