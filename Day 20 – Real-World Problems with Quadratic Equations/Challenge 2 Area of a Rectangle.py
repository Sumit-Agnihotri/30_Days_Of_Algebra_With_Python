from sympy import symbols, Eq, solve

x = symbols('x')
area_expr = x * (x - 2)
equation = Eq(area_expr, 60)
sol = solve(equation, x)

for s in sol:
    if s > 2:
        print("Length:", s, ", Width:", s - 2)