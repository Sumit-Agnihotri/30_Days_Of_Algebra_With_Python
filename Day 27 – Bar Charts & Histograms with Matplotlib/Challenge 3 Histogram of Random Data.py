import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)  # Mean = 0, Std Dev = 1

plt.hist(data, bins=30, edgecolor='black')
plt.title("Normal Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()