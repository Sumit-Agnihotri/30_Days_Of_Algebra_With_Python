import matplotlib.pyplot as plt

cities = ['Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Kolkata']
population = [18, 20, 12, 10, 14]  # In millions

plt.barh(cities, population, color='skyblue')
plt.title("City Populations")
plt.xlabel("Population (millions)")
plt.ylabel("Cities")
plt.grid(True)
plt.show()