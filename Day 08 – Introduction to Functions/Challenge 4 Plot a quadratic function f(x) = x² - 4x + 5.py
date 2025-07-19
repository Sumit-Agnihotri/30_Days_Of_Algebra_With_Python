import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(-2, 6, 10)
b = a**2 - 4*a + 5

plt.plot(a, b, label='f(x) = a² - 4a + 5')
plt.title('Plot of the function f(x) = aa² - 4a + 5')
plt.xlabel('a')
plt.ylabel('f(a)')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.legend()
plt.show()