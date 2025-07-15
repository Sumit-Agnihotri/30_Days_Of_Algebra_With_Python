from sympy import symbols, Eq, solve

def solve_linear_equation(a, b, c):
    x = symbols('x')
    equation = Eq(a * x + b, c)
    solution = solve(equation)
    return solution[0] if solution else None

result = solve_linear_equation(4, 2, 10)
if result is not None:
    print("x =", result)
else:
    print("No solution found.")