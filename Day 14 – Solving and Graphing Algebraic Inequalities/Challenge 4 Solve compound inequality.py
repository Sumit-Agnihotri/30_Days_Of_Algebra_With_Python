from sympy import symbols, And, solve_univariate_inequality
from sympy import S

x = symbols('x')
inequality = And(x > 2, x <= 5)

solution = solve_univariate_inequality(inequality, x, relational=False, domain=S.Reals)
print("Solution:", solution)