from sympy import symbols, Eq, solve

x, y = symbols('x y')
eq1 = Eq(2*x + y, 8)
eq2 = Eq(3*x - y, 1)

solution = solve((eq1, eq2), (x, y))
print("Solution:", solution)