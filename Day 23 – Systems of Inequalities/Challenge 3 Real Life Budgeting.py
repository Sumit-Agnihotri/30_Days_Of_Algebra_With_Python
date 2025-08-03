from sympy import symbols, Eq, And, solve

p, n = symbols('p n', integer=True)

ineq1 = 20*p + 50*n <= 500
ineq2 = p >= 3

possible = []
for pens in range(3, 26):
    max_notebooks = (500 - 20*pens) // 50
    if max_notebooks >= 0:
        possible.append((pens, max_notebooks))

print("Some valid (Pens, Notebooks):", possible[:5], "...")