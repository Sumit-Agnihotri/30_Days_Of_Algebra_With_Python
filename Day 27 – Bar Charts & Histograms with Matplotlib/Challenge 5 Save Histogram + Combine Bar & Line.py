import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Mean = 0, Std Dev = 1
# Save histogram
plt.hist(data, bins=20, edgecolor='black')
plt.title("Saved Histogram")
plt.savefig("histogram_output.png")
plt.close()

# Combine bar and line
categories = ['Q1', 'Q2', 'Q3', 'Q4']
revenue = [50, 65, 70, 80]
growth = [5, 7, 6, 8]

plt.bar(categories, revenue, color='lightgreen', label="Revenue (₹K)")
plt.plot(categories, growth, color='blue', marker='o', label="Growth (%)")

plt.title("Quarterly Revenue & Growth")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()