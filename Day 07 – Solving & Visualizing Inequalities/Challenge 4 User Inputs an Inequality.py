from sympy import symbols, solve_univariate_inequality, sympify

x = symbols('x')

user_input = input("Enter inequality (e.g., x + 5 < 12): ")
inequality = sympify(user_input)

solution = solve_univariate_inequality(inequality, x, relational=False)
print("Solution:", solution)