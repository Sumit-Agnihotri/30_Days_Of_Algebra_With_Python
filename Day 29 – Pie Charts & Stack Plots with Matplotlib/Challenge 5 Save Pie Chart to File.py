import matplotlib.pyplot as plt

companies = ['Apple', 'Samsung', 'Xiaomi', 'Others']
market_share = [40, 30, 20, 10]
colors = ['gold', 'skyblue', 'lightgreen', 'lightcoral']

plt.pie(market_share, labels=companies, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Market Share Report")
plt.savefig("market_share_pie.png")
plt.close()