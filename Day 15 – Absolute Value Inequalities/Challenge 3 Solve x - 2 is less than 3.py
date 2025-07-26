from sympy import Abs, S, symbols
from sympy.solvers.inequalities import solve_univariate_inequality

x = symbols('x')
inequality = Abs(x - 2) < 3
solution = solve_univariate_inequality(inequality, x, relational=False, domain=S.Reals)
print("Solution:", solution)