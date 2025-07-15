from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(2 * x + 3, 7)
solution = solve(equation)
print(f"The solution to the equation 2x + 3 = 7 is x = {solution[0]}")