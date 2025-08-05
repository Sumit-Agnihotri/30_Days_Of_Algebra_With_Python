from sympy import symbols, solve_univariate_inequality, S

x = symbols('x')
inequality = (x**2 + 4*x + 3) <= 0
solution = solve_univariate_inequality(inequality, x, domain=S.Reals)
print("Solution:", solution)