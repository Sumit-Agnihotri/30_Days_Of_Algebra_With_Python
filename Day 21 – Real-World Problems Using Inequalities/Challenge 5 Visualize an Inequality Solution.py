from sympy import solve_univariate_inequality, symbols
from sympy import S

x = symbols('x')
inequality = x**2 - 4 < 5
solution = solve_univariate_inequality(inequality, x, domain=S.Reals)

print("Solution set:", solution)