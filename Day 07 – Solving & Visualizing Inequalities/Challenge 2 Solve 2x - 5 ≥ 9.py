from sympy import symbols, solve_univariate_inequality, Ge

x = symbols('x')
inequality = Ge(2 * x - 5, 9)

solution = solve_univariate_inequality(inequality, x, relational=False)
print("Solution:", solution)