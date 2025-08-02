from sympy import symbols, Eq, solve

x = symbols('x')
cost = 1000 + 50*x
revenue = 70*x

eq = Eq(cost, revenue)
solution = solve(eq, x)
print("Break-even at units:", solution[0])