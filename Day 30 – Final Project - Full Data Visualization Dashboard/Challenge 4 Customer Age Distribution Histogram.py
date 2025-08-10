import numpy as np
import matplotlib.pyplot as plt

ages = np.random.randint(18, 60, 200)

plt.hist(ages, bins=10, edgecolor='black', color='orange')
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()