from sympy import symbols, Eq, solve

x = symbols('x')
eq = Eq(3 / (10 + x), 0.2)  # 3 liters of salt stays constant
solution = solve(eq, x)
print("Water to add (liters):", solution[0])