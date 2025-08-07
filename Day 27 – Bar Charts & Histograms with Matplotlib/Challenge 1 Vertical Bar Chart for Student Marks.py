import matplotlib.pyplot as plt

names = ['Alice', 'Bob', 'Charlie', 'Diana']
marks = [85, 78, 92, 88]

plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()