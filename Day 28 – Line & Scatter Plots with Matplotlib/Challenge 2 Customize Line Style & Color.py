import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 180, 170, 200, 210, 190]

plt.plot(months, sales, color='green', linestyle='--', marker='s', linewidth=2)
plt.title("Styled Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales (in ₹K)")
plt.grid(True)
plt.show()