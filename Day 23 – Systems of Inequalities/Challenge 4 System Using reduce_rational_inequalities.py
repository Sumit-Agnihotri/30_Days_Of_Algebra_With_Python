from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import symbols

x = symbols('x')
inequality = [[(1/x > 0), (x < 3)]]

solution = reduce_rational_inequalities(inequality, x)
print("Solution:", solution)
