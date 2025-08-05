from sympy import symbols, solve_univariate_inequality, S

x = symbols('x')
inequality = (-2*x**2 + 8*x - 6) >= 0
solution = solve_univariate_inequality(inequality, x, domain=S.Reals)
print("Solution:", solution)