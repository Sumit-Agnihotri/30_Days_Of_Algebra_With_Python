import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_a = [150, 180, 170, 200, 210, 190]
product_b = [140, 160, 165, 180, 195, 185]

plt.plot(months, product_a, marker='o', label="Product A")
plt.plot(months, product_b, marker='^', label="Product B")
plt.title("Product Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales (in ₹K)")
plt.legend()
plt.grid(True)
plt.show()