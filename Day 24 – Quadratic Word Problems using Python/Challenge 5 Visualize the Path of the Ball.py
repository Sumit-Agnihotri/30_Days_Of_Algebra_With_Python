import numpy as np
import matplotlib.pyplot as plt

t_vals = np.linspace(0, 4.5, 100)
h_vals = -5 * t_vals**2 + 20 * t_vals

plt.plot(t_vals, h_vals, label='h(t) = -5t² + 20t')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title("Projectile Motion of a Ball")
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.grid(True)
plt.legend()
plt.show()