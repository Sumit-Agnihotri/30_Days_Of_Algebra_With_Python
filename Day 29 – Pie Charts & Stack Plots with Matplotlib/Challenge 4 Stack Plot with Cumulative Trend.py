import matplotlib.pyplot as plt

weeks = [1, 2, 3, 4, 5]
team_a = [5, 6, 7, 8, 9]
team_b = [3, 4, 4, 5, 6]
team_c = [2, 3, 3, 4, 4]

plt.stackplot(weeks, team_a, team_b, team_c, labels=['Team A', 'Team B', 'Team C'], colors=['#FF9999', '#66B2FF', '#99FF99'])
plt.title("Cumulative Project Hours by Team")
plt.xlabel("Weeks")
plt.ylabel("Hours")
plt.legend(loc='upper left')
plt.show()