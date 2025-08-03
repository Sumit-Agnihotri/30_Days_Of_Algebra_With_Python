from sympy import symbols, solve_univariate_inequality, S, Interval

x = symbols('x')
sol1 = solve_univariate_inequality(x >= 2, x, relational=False, domain=S.Reals)
sol2 = solve_univariate_inequality(x + 3 <= 10, x, relational=False, domain=S.Reals)

solution = sol1.intersect(sol2)

print("Solution for x:", solution)