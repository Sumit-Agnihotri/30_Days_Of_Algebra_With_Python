from sympy import symbols, Eq, solve

x = symbols('x')
side = 12
total_area = (side + 2*x)**2
equation = Eq(total_area, 196)

sol = solve(equation, x)
print("Width of walkway:", [s for s in sol if s > 0][0])