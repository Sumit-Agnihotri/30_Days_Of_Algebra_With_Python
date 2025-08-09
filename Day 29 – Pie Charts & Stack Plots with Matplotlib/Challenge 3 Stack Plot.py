import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
math = [2, 3, 2, 4, 3, 2, 1]
science = [1, 2, 3, 2, 2, 3, 2]
english = [2, 1, 2, 1, 2, 1, 3]

plt.stackplot(days, math, science, english, labels=['Math', 'Science', 'English'], colors=['gold', 'skyblue', 'lightgreen'])
plt.title("Study Hours per Subject in a Week")
plt.legend(loc='upper left')
plt.show()