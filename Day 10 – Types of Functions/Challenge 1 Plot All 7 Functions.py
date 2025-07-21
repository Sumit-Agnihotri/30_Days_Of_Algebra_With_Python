# challenge1_plot_functions.py
import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-10, 10, 400)

functions = {
    "Constant": lambda x: np.full_like(x, 5),
    "Identity": lambda x: x,
    "Linear": lambda x: 2 * x + 3,
    "Quadratic": lambda x: x**2 - 4 * x + 3,
    "Cubic": lambda x: x**3,
    "Absolute": lambda x: np.abs(x),
    "Step (floor)": lambda x: np.floor(x)
}

for name, func in functions.items():
    plt.figure()
    plt.plot(x_vals, func(x_vals), label=name)
    plt.title(f"{name} Function")
    plt.grid()
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.legend()
    plt.show()