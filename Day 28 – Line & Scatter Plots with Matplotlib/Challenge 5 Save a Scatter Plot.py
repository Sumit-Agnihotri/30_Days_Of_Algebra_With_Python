import numpy as np
import matplotlib.pyplot as plt

hours_studied = np.random.randint(1, 10, 20)
exam_scores = hours_studied * 10 + np.random.randint(-5, 5, 20)

plt.scatter(hours_studied, exam_scores, color='orange', edgecolors='black')
plt.title("Saved Scatter Plot")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)
plt.savefig("scatter_plot.png")
plt.close()