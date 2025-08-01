from sympy import symbols, solve_univariate_inequality
from sympy import S

x = symbols('x')
inequality = 25 * x <= 200
solution = solve_univariate_inequality(inequality, x, domain=S.Integers)

print("Max notebooks allowed:", solution)