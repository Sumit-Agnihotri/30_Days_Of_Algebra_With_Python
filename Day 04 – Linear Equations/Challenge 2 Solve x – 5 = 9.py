from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(x - 5, 9)
solution = solve(equation)
print(f"The solution to the equation x - 5 = 9 is x = {solution[0]}")