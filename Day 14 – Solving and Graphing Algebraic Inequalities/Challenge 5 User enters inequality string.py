from sympy import symbols, solve_univariate_inequality, sympify
from sympy import S

x = symbols('x')
user_input = input("Enter an inequality in x (e.g., x**2 - 4 < 0): ")
ineq = sympify(user_input)

solution = solve_univariate_inequality(ineq, x, relational=False, domain=S.Reals)
print("Solution:", solution)