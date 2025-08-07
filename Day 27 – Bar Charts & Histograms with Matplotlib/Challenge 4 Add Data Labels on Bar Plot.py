import matplotlib.pyplot as plt

values = [25, 40, 30, 55]
labels = ['Product A', 'Product B', 'Product C', 'Product D']

plt.bar(labels, values, color='coral')
plt.title("Sales by Product")
plt.xlabel("Products")
plt.ylabel("Sales (in ₹K)")

# Add labels on bars
for i, v in enumerate(values):
    plt.text(i, v + 1, str(v), ha='center')

plt.show()