from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(x**3 - 8, 0)
solutions = solve(equation, x)
print("Solutions:", solutions)