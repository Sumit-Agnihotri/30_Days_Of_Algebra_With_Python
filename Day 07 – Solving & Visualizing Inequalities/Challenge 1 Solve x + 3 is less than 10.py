from sympy import symbols, solve_univariate_inequality, Lt

x = symbols('x')
inequality = Lt(x + 3, 10)

solution = solve_univariate_inequality(inequality, x, relational=False)
print("Solution:", solution)