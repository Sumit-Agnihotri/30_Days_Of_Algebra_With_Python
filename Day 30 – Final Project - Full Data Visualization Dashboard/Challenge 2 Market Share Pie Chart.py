import matplotlib.pyplot as plt

companies = ['Apple', 'Samsung', 'Xiaomi', 'Others']
market_share = [40, 30, 20, 10]
colors = ['gold', 'skyblue', 'lightgreen', 'lightcoral']
explode = (0.1, 0, 0, 0)

plt.pie(market_share, labels=companies, autopct='%1.1f%%', startangle=90, explode=explode, colors=colors, shadow=True)
plt.title("Market Share Distribution")
plt.show()