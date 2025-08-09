import matplotlib.pyplot as plt

companies = ['Apple', 'Samsung', 'Xiaomi', 'Others']
market_share = [40, 30, 20, 10]

plt.pie(market_share, labels=companies)
plt.title("Market Share - Smartphone Industry")
plt.show()