import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)
hours_studied = rng.integers(1, 10, 20)
exam_scores = hours_studied * 10 + rng.integers(-5, 5, 20)

plt.scatter(hours_studied, exam_scores, color='orange', edgecolors='black')
plt.title("Saved Scatter Plot")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)
plt.savefig("scatter_plot.png")
plt.close()