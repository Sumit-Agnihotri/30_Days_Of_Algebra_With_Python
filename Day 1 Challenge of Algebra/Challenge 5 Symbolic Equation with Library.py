from sympy import Eq, symbols, solve

x = symbols('x')
expression = 2*x + 3
equation = Eq(expression, 0)
solution = solve(equation, x)
print(f"The solution to the equation {expression} = 0 is x = {solution[0]}")