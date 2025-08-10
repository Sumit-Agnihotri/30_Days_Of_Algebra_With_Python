import matplotlib.pyplot as plt

products = ['Laptop', 'Tablet', 'Phone', 'Monitor']
sales = [250, 180, 300, 150]

plt.bar(products, sales, color='skyblue')
plt.title("Q1 Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.show()