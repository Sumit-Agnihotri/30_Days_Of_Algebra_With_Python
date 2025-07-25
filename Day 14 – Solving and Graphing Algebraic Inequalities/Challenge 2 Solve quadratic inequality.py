from sympy import symbols, solve_univariate_inequality
from sympy import S

x = symbols('x')
inequality = x**2 - 4 < 0

solution = solve_univariate_inequality(inequality, x, relational=False, domain=S.Reals)
print("Solution:", solution)