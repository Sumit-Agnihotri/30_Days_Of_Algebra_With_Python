import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(-10, 10, 100)
b = 2 * a + 3

plt.plot(a, b, label='f(a) = 2a + 3')
plt.title('Plot of the function f(a) = 2a + 3')
plt.xlabel('a')
plt.ylabel('f(a)')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.legend()
plt.show()