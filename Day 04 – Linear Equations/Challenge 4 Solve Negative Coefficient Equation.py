from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(-3 * x + 6, 0)
solution = solve(equation)
print(f"The solution to the equation -3x + 6 = 0 is x = {solution[0]}")