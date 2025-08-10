import matplotlib.pyplot as plt
import numpy as np

products = ['Laptop', 'Tablet', 'Phone', 'Monitor']
sales = [250, 180, 300, 150]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue = [2000, 2500, 2700, 3000, 3500]
companies = ['Apple', 'Samsung', 'Xiaomi', 'Others']
market_share = [40, 30, 20, 10]
colors = ['gold', 'skyblue', 'lightgreen', 'lightcoral']
explode = (0.1, 0, 0, 0)
ages = np.random.randint(18, 60, 200)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Bar Chart
axs[0, 0].bar(products, sales, color='skyblue')
axs[0, 0].set_title("Q1 Product Sales")

# Pie Chart
axs[0, 1].pie(market_share, labels=companies, autopct='%1.1f%%', startangle=90, explode=explode, colors=colors, shadow=True)
axs[0, 1].set_title("Market Share")

# Line Plot
axs[1, 0].plot(months, revenue, marker='o', color='green')
axs[1, 0].set_title("Monthly Revenue Trend")
axs[1, 0].grid(True)

# Histogram
axs[1, 1].hist(ages, bins=10, edgecolor='black', color='orange')
axs[1, 1].set_title("Customer Age Distribution")

plt.tight_layout()
plt.savefig("final_dashboard.png")
plt.show()