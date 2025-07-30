from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(2*x**2 + 8*x, 0)
solutions = solve(equation, x)
print("Solutions:", solutions)