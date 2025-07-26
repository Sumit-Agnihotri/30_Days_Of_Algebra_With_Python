from sympy import symbols, Abs, solve_univariate_inequality, S

x = symbols('x')
inequality = Abs(x) < 4

solution = solve_univariate_inequality(inequality, x, relational=False, domain=S.Reals)
print("Solution:", solution)