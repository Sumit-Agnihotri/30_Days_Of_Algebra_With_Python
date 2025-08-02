from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')
eq1 = Eq(x + y + z, 6)
eq2 = Eq(2*x - y + z, 3)
eq3 = Eq(x + 2*y - z, 3)

solution = solve((eq1, eq2, eq3), (x, y, z))
print("Solution:", solution)