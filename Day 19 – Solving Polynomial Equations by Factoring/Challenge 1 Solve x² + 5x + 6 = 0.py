from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(x**2 + 5*x + 6, 0)

solutions = solve(equation, x)
print("Solutions:", solutions)