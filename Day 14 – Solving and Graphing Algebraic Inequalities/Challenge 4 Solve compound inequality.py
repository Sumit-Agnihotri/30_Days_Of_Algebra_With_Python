from sympy import symbols, solve_univariate_inequality, S
from sympy.sets import Intersection

x = symbols('x')

ineq1 = solve_univariate_inequality(x > 2, x, relational=False, domain=S.Reals)
ineq2 = solve_univariate_inequality(x <= 5, x, relational=False, domain=S.Reals)

solution = Intersection(ineq1, ineq2)

print("Solution:", solution)