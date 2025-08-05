from sympy import symbols, solve_univariate_inequality, S

x = symbols('x')
inequality = (x*(x + 5)) > 24
solution = solve_univariate_inequality(inequality, x, domain=S.Reals)
print("Solution:", solution)