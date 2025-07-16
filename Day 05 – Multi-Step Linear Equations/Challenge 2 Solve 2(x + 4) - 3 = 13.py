from sympy import Eq, solve, symbols

x = symbols('x')
equation = Eq(2 * (x + 4) - 3, 13)
solution = solve(equation, x)
print("The value of x is:", solution[0])